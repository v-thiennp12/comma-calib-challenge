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
model                   = keras.models.load_model("model-resnet-mod-015.h5")
batch_size              = 15
is_training             = False

#Evaluate and display the prediction
data_dir_test           = 'labeled/4' 
x_test, y_test          = utils.load_csv('labeled','4_tiff.csv')
eval_batch              = batch_generator_2inputs(data_dir_test, x_test, y_test, batch_size, is_training)
prediction_performance  = model.evaluate(eval_batch)
print(data_dir_test)
print(model.metrics_names)
print(prediction_performance)

data_dir_test           = 'labeled/3' 
x_test, y_test          = utils.load_csv('labeled','3_tiff.csv')
eval_batch              = batch_generator_2inputs(data_dir_test, x_test, y_test, batch_size, is_training)
prediction_performance  = model.evaluate(eval_batch)
print(data_dir_test)
print(model.metrics_names)
print(prediction_performance)

data_dir_test           = 'labeled/2' 
x_test, y_test          = utils.load_csv('labeled','2_tiff.csv')
eval_batch              = batch_generator_2inputs(data_dir_test, x_test, y_test, batch_size, is_training)
prediction_performance  = model.evaluate(eval_batch)
print(data_dir_test)
print(model.metrics_names)
print(prediction_performance)

data_dir_test           = 'labeled/1' 
x_test, y_test          = utils.load_csv('labeled','1_tiff.csv')
eval_batch              = batch_generator_2inputs(data_dir_test, x_test, y_test, batch_size, is_training)
prediction_performance  = model.evaluate(eval_batch)
print(data_dir_test)
print(model.metrics_names)
print(prediction_performance)

data_dir_test           = 'labeled/0' 
x_test, y_test          = utils.load_csv('labeled','0_tiff.csv')
eval_batch              = batch_generator_2inputs(data_dir_test, x_test, y_test, batch_size, is_training)
prediction_performance  = model.evaluate(eval_batch)
print(data_dir_test)
print(model.metrics_names)
print(prediction_performance)