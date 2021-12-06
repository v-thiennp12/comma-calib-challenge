# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:57:33 2021

@author: nguye
"""


import utils

# extract frames from video
# video = 'labeled/2.hevc'
# output_path = 'C:\opticalflow\calib_challenge-main'
# utils.video2frame(video, output_path, 0)

# read csv
x_train, y_train = utils.load_csv('C:\opticalflow\calib_challenge-main\labeled','0.csv')
print(x_train, y_train)

x_test, y_test = utils.load_csv('C:\opticalflow\calib_challenge-main\labeled','1.csv')
print(x_test, y_test)