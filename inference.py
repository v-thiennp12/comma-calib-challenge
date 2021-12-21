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

#Load saved model
model = keras.models.load_model("model-resnet-mod-015.h5")

#Evaluate and display the prediction
data_dir_test           = 'labeled/4' 
x_test, y_test          = utils.load_csv('labeled','1_tiff.csv')

prediction_performance  = model.evaluate(data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)
dict(zip(reconstructed.metrics_names, prediction_performance))