#tensorflow and keras
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.utils import plot_model
from keras import regularizers, activations
from keras.models import Sequential, Model
from keras.layers import Input, Flatten, Dense, Dropout, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D, GlobalAveragePooling2D, ZeroPadding2D, Concatenate
from keras.layers import Lambda, Activation
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
print ("TensorFlow version: " + tf.__version__)

#utils
import numpy as np
import cv2 as cv
import uuid
from matplotlib.colors import hsv_to_rgb
from utils import IMAGE_HEIGHT, IMAGE_WIDTH, INPUT_SHAPE, batch_generator, batch_generator_2inputs
import utils

def build_model():
    """
    Modified NVIDIA model
    """

    # IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 66, 200, 3
    # INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)
    keep_prob   = 0.55

    in_a  = Input(shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3), name = 'current_frame')    
    in_b  = Input(shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3), name = 'previous_frame')

    norm_a = Lambda(lambda x: x/127.5-1.0, input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3))(in_a)
    norm_b = Lambda(lambda x: x/127.5-1.0, input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3))(in_b)

    conv1a = Conv2D(64,  kernel_size=7, strides=2, padding='same', use_bias=True, activation='tanh')(norm_a)
    conv2a = Conv2D(128, kernel_size=5, strides=2, padding='same', use_bias=True, activation='tanh')(conv1a)
    conv3a = Conv2D(256, kernel_size=5, strides=2, padding='same', use_bias=True, activation='tanh')(conv2a)

    conv1b = Conv2D(64,  kernel_size=7, strides=2, padding='same', use_bias=True, activation='tanh')(norm_b)
    conv2b = Conv2D(128, kernel_size=5, strides=2, padding='same', use_bias=True, activation='tanh')(conv1b)
    conv3b = Conv2D(256, kernel_size=5, strides=2, padding='same', use_bias=True, activation='tanh')(conv2b)    

    in_conv4    = Concatenate(axis=1)([conv3a, conv3b])
    conv4       = Conv2D(256, kernel_size=1, strides=1, padding='same', use_bias=True, activation='tanh')(in_conv4)
    conv5       = Conv2D(512, kernel_size=4, strides=4, padding='same', use_bias=True, activation='tanh')(conv4)
    conv6       = Conv2D(512, kernel_size=4, strides=4, padding='same', use_bias=True, activation='tanh')(conv5)

    flatted     = Flatten()(conv6)
    dense       = Dense(1)(flatted)

    model       = Model([in_a, in_b], dense, name="FlowNet_corr")
    model.summary()
    plot_model(model, "./model.png", show_shapes=True)    
    return model

def train_model(model, x_train, x_valid, y_train, y_valid):
    """
    Train the model
    # """
    # data_dir_train      = 'C:\\opticalflow\\calib_challenge-main\\labeled\\0'
    # data_dir_test       = 'C:\\opticalflow\\calib_challenge-main\\labeled\\1'

    data_dir_train      = 'labeled/0'
    data_dir_test       = 'labeled/1'    

    epochs              = 10
    samples_per_epoch   = 1000 #250
    batch_size          = 15   #40
    learning_rate       = 1.0E-4
    
    checkpoint = ModelCheckpoint('model-{epoch:03d}.h5',
                                 monitor='val_loss',
                                 verbose=0,
                                 save_best_only=True,
                                 mode='auto')

    model.compile(loss='mean_squared_error', optimizer='Adam')

    model.fit_generator(batch_generator_2inputs(data_dir_train, x_train, y_train, batch_size, True),
            samples_per_epoch,
            epochs,
            max_queue_size=1,
            validation_data=batch_generator(data_dir_test, x_valid, y_valid, batch_size, False),
            validation_steps=len(x_valid),
            callbacks=[checkpoint],
            verbose=1)

if __name__ == '__main__':
    
    #build nvidia-pilotnet model
    model               = build_model()
    
    # # read csv
    # x_train, y_train    = utils.load_csv('C:\\opticalflow\\calib_challenge-main\\labeled','0_tiff.csv')     
    # x_test, y_test      = utils.load_csv('C:\\opticalflow\\calib_challenge-main\\labeled','1_tiff.csv')
    # print(x_train, y_train)   
    # print(x_test, y_test)
    x_train, y_train    = utils.load_csv('labeled','0_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','1_tiff.csv')    
    
    #
    train_model(model, x_train, x_test, y_train, y_test)