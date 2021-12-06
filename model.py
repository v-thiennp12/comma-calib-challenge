#tensorflow and keras
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.utils import plot_model
from keras import regularizers, activations
from keras.models import Sequential, Model
from keras.layers import Input, Flatten, Dense, Dropout, BatchNormalization
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D, GlobalAveragePooling2D, ZeroPadding2D
from keras.layers import Lambda, Activation
from keras.callbacks import ModelCheckpoint
from keras.preprocessing.image import ImageDataGenerator
# from keras.optimizers import Adam, SGD
print ("TensorFlow version: " + tf.__version__)

#utils
import numpy as np
import cv2 as cv
import uuid
from matplotlib.colors import hsv_to_rgb
from utils import INPUT_SHAPE, batch_generator
import utils

def build_model():
    """
    Modified NVIDIA model
    """

    # IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 66, 200, 3
    # INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)
    keep_prob   = 0.75

    model = Sequential()
    model.add(Lambda(lambda x: x/127.5-1.0, input_shape=INPUT_SHAPE))
    model.add(Conv2D(24, kernel_size=(5,5), strides=(2,2), activation='elu'))
    model.add(Conv2D(36, kernel_size=(5,5), strides=(2,2), activation='elu'))
    model.add(Conv2D(48, kernel_size=(5,5), strides=(2,2), activation='elu'))
    model.add(Conv2D(64, kernel_size=(3,3), strides=(1,1), activation='elu'))
    model.add(Conv2D(64, kernel_size=(3,3), strides=(1,1), activation='elu'))
    model.add(Dropout(keep_prob))
    model.add(Flatten())
    model.add(Dense(100, activation='elu'))
    model.add(Dense(50, activation='elu'))
    model.add(Dense(10, activation='elu'))
    model.add(Dense(1))

    model.summary()  
    # plot_model(model, "figures/model.png", show_shapes=True)    
    return model

def train_model(model, x_train, x_valid, y_train, y_valid):
    """
    Train the model
    """
    data_dir_train      = 'C:\\opticalflow\\calib_challenge-main\\labeled\\0_'
    data_dir_test       = 'C:\\opticalflow\\calib_challenge-main\\labeled\\1_'
    epochs              = 10
    samples_per_epoch   = 250
    batch_size          = 40
    learning_rate       = 1.0E-4
    
    checkpoint = ModelCheckpoint('model-{epoch:03d}.h5',
                                 monitor='val_loss',
                                 verbose=0,
                                 save_best_only=True,
                                 mode='auto')

    model.compile(loss='mean_squared_error', optimizer='Adam')

    model.fit_generator(batch_generator(data_dir_train, x_train, y_train, batch_size, True),
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
    
    # read csv
    x_train, y_train    = utils.load_csv('C:\\opticalflow\\calib_challenge-main\\labeled','0.csv')
    # print(x_train, y_train)    
    x_test, y_test      = utils.load_csv('C:\opticalflow\calib_challenge-main\labeled','1.csv')
    # print(x_test, y_test)
    
    #
    train_model(model, x_train, x_test, y_train, y_test)
    
    