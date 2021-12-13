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
#load frame
# frame = 'labeled/2/0.tiff'
# utils.load_framestack(frame)

####
# # read csv
# x_train, y_train = utils.load_csv('C:\opticalflow\calib_challenge-main\labeled','0.csv')
# print(x_train, y_train)

# x_test, y_test = utils.load_csv('C:\opticalflow\calib_challenge-main\labeled','1.csv')
# print(x_test, y_test)