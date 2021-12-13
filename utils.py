#author : naokishibuya
#folked from : https://github.com/naokishibuya/car-behavioral-cloning

import os, uuid
import numpy as np
import cv2
import pandas as pd
import pickle
import matplotlib.image as mpimg
from matplotlib.colors import hsv_to_rgb

IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 874, 1164, 6
INPUT_SHAPE     = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)

def video2frame(video_file, output_path, reshape):
    dir_path, file_name = os.path.split(video_file)
    path, ext           = os.path.splitext(video_file)
    
    frame_dir           = path[-1]
    os.makedirs(os.path.join(output_path, dir_path, frame_dir), exist_ok=True)

    cap                 = cv2.VideoCapture(video_file)
    ret, frame          = cap.read()    
    
    count               = 0  
    while(ret):
        frame_name      = os.path.join(output_path, dir_path, frame_dir, str(count) + ".png")        
        cv2.imwrite(frame_name, frame)
        ret, frame      = cap.read()
        count           += 1
        # print(frame_name) # print(count, ret, frame)
    cap.release()

def video2framestack(video_file, output_path, reshape):
    dir_path, file_name = os.path.split(video_file)
    path, ext           = os.path.splitext(video_file)
    
    frame_dir           = path[-1]
    os.makedirs(os.path.join(output_path, dir_path, frame_dir), exist_ok=True)

    cap                 = cv2.VideoCapture(video_file)
    ret, frame          = cap.read()
    prev_frame          = frame
    
    count               = 0  
    while(ret):
        frame_name      = os.path.join(output_path, dir_path, frame_dir, str(count) + ".tiff")
        frame_stack     = np.concatenate((frame, prev_frame), axis=2)

        with open(frame_name, "wb") as f_out:
            pickle.dump(frame_stack, f_out)
            
        prev_frame      = frame
        ret, frame      = cap.read()
        count           += 1
        print(frame_name)
        # print(count, ret)
        print(frame_stack.shape)
    cap.release()

def load_framestack(framestack_file):
    with open(framestack_file, "rb") as f_in:
        frame_stack = pickle.load(f_in)        
        # print(frame_stack.shape)
        # cv2.imshow('__', frame_stack[...,:3])
        # cv2.waitKey(2000)
        # cv2.destroyAllWindows()
    return frame_stack
    
def load_csv(data_dir, csv_file):
    """
    Load training data and split it into training and validation set
        # X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=args.test_size, random_state=0)
    """
    data_df = pd.read_csv(os.path.join(data_dir, csv_file))

    x = data_df['image'].values
    y = data_df[['pitch', 'yaw']].values    

    return x, y
    
def load_image(data_dir, image_file):
    """
    Load RGB images from a file
    """
    # print('data_dir', data_dir)
    print(os.path.join(data_dir.strip(), image_file.strip()))
    return mpimg.imread(os.path.join(data_dir, image_file.strip()))

def crop(image):
    """
    Crop the image (removing the sky at the top and the car front at the bottom)
    """
    return image[60:-25, :, :] # remove the sky and the car front

def resize(image):
    """
    Resize the image to the input shape used by the network model
    """
    return cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT), cv2.INTER_AREA)

def rgb2yuv(image):
    """
    Convert the image from RGB to YUV (This is what the NVIDIA model does)
    """
    return cv2.cvtColor(image, cv2.COLOR_RGB2YUV)

def preprocess(image):
    """
    Combine all preprocess functions into one
    """
    image = crop(image)
    image = resize(image)
    image = rgb2yuv(image)
    return image

def random_flip(image, pitch_angle):
    """
    Randomly flipt the image left <-> right, and adjust the pitch_angle angle.
    """
    #pitch angle is not affected by flipped image
    
    if np.random.rand() < 0.5:
        image       = cv2.flip(image, 1)
        pitch_angle = pitch_angle
    return image, pitch_angle

def random_shadow(image):
    """
    Generates and adds random shadow
    """
    # (x1, y1) and (x2, y2) forms a line
    # xm, ym gives all the locations of the image
    x1, y1 = IMAGE_WIDTH * np.random.rand(), 0
    x2, y2 = IMAGE_WIDTH * np.random.rand(), IMAGE_HEIGHT
    xm, ym = np.mgrid[0:IMAGE_HEIGHT, 0:IMAGE_WIDTH]

    # mathematically speaking, we want to set 1 below the line and zero otherwise
    # Our coordinate is up side down.  So, the above the line: 
    # (ym-y1)/(xm-x1) > (y2-y1)/(x2-x1)
    # as x2 == x1 causes zero-division problem, we'll write it in the below form:
    # (ym-y1)*(x2-x1) - (y2-y1)*(xm-x1) > 0
    
    # print(image)
    mask = np.zeros_like(image[:, :, 1])
    mask[(ym - y1) * (x2 - x1) - (y2 - y1) * (xm - x1) > 0] = 1

    # choose which side should have shadow and adjust saturation
    cond = mask == np.random.randint(2)
    s_ratio = np.random.uniform(low=0.2, high=0.5)

    # adjust Saturation in HLS(Hue, Light, Saturation)
    hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
    hls[:, :, 1][cond] = hls[:, :, 1][cond] * s_ratio
    return cv2.cvtColor(hls, cv2.COLOR_HLS2RGB)

def random_brightness(image):
    """
    Randomly adjust brightness of the image.
    """
    # HSV (Hue, Saturation, Value) is also called HSB ('B' for Brightness).
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    ratio = 1.0 + 0.4 * (np.random.rand() - 0.5)
    hsv[:,:,2] =  hsv[:,:,2] * ratio
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

def augment(image, pitch_angle, range_x=100, range_y=10):
    """
    Generate an augmented image and adjust steering angle.
    (The steering angle is associated with the center image)
    """
    image, pitch_angle  = random_flip(image, pitch_angle)
    image               = random_shadow(image)
    image               = random_brightness(image)
    return image, pitch_angle

def batch_generator(data_dir, image_paths, angles, batch_size, is_training):
    """
    Generate training image give image paths and associated steering angles
    """
    # print('data_dir', data_dir)
    images  = np.empty([batch_size, IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS])
    pitches = np.empty(batch_size)
    while True:
        i = 0
        #angles[index][0] pitch | angles[index][1] yaw
        for index in np.random.permutation(image_paths.shape[0]):
            # print('data_dir', data_dir)
            image               = load_framestack(os.path.join(data_dir, image_paths[index]))
            pitch_angle         = angles[index][0]

            # image               = load_image(data_dir, image_paths[index]) *
            # pitch_angle         = angles[index][0] *
            
            # image               = image_paths[index]
            # pitch_angle         = angles[index][0]
            
            # # augmentation
            # if is_training and np.random.rand() < 0.6:*
            #     image, pitch_angle = augment(image, pitch_angle)*
            # else:
            #     image = load_image(data_dir, image)
            
            # add the image and pitch angle to the batch
            # images[i]   = preprocess(image)*
            pitches[i]  = pitch_angle
            i += 1
            if i == batch_size:
                break
        yield images, pitches