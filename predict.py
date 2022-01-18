#tensorflow and keras
import tensorflow as tf
import tensorflow.keras as keras
print ("TensorFlow version: " + tf.__version__)

#utils
import uuid, os, glob
from utils import IMAGE_HEIGHT, IMAGE_WIDTH, INPUT_SHAPE
import utils
import uuid

#Load saved model
model                   = keras.models.load_model("model-resnet-mod-2-030.h5")

#Evaluate and display the prediction
data_dir_test           = './labeled/4' 
# image_paths             = os.listdir(data_dir_test)
image_paths             = glob.glob(data_dir_test + '/*.tiff')

print(data_dir_test)
print(image_paths)

output_dict             = []

index                   = 0
while (index < len(image_paths)):
    # image               = load_framestack(os.path.join(data_dir_test, image_paths[index]))
    image               = utils.load_framestack(os.path.join(image_paths[index]))

    # print(image.shape)
    #     874 x 1164 x 3
    image_a             = image[...,:3]
    image_b             = image[...,3:]
    # 1 x 874 x 1164 x 3
    image_a             = image_a[None, ...]
    image_b             = image_b[None, ...]
    # print(image_a.shape)
    # print(image_b.shape)

    predict             = model.predict([image_a, image_b])

    print(image_paths[index], '- pitch predicted ', predict)
    output_dict.append({'frame': index, 'prediction - pitch': predict})

    index               += 1

print(output_dict)
output_name             = 'prediction_' + uuid.uuid1().hex + '.txt'
with open(output_name, 'w') as f:
    print(data_dir_test)
    print(output_dict, file=f)