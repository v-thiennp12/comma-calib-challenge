# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:57:33 2021

@author: nguye
"""


import utils

####
# extract single-frames from video
# video = 'labeled/2.hevc'
# output_path = 'C:\\opticalflow\\calib_challenge-main' ''
# utils.video2frame(video, output_path, 0)

####
# extract and stack 2 consecutive frames from video
# current frame and previous are stacked together
# video = 'labeled/0.hevc'
# output_path = ''
# utils.video2framestack(video, output_path, 0)

# video = 'labeled/1.hevc'
# output_path = ''
# utils.video2framestack(video, output_path, 0)

# video = 'labeled/2.hevc'
# output_path = ''
# utils.video2framestack(video, output_path, 0)

# video = 'labeled/3.hevc'
# output_path = ''
# utils.video2framestack(video, output_path, 0)

# video = 'labeled/4.hevc'
# output_path = ''
# utils.video2framestack(video, output_path, 0)

####
# extract and stack 2 consecutive frames from video
# current frame and previous are stacked together
video = 'unlabeled/5.hevc'
output_path = ''
utils.video2framestack(video, output_path, 0)

video = 'unlabeled/6.hevc'
output_path = ''
utils.video2framestack(video, output_path, 0)

video = 'unlabeled/7.hevc'
output_path = ''
utils.video2framestack(video, output_path, 0)

video = 'unlabeled/8.hevc'
output_path = ''
utils.video2framestack(video, output_path, 0)

video = 'unlabeled/9.hevc'
output_path = ''
utils.video2framestack(video, output_path, 0)

####
#load frame
# frame = 'labeled/2/0.tiff'
# utils.load_framestack(frame)

####
# # read csv
# x_train, y_train = utils.load_csv('C:\opticalflow\calib_challenge-main\labeled','0.csv')
# print(x_train, y_train)

# x_test, y_test = utils.load_csv('C:\opticalflow\calib_challenge-main\labeled','1.csv')
# print(x_test, y_test)

# x_train, y_train    = utils.load_csv('labeled','2_tiff.csv')     
# x_test, y_test      = utils.load_csv('labeled','1_tiff.csv')

# print(y_train.shape)
# print(x_test.shape)

# import numpy as np
# # for ij in range(y_train.shape[0]):
#     # print(y_train[ij])
#     # print(x_train[ij])
#     # if ((np.isnan(y_train[ij][0])) or (np.isnan(y_train[ij][1]))):
#     #     print(y_train[ij])