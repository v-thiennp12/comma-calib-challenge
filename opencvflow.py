# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:40:51 2021

@author: https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html
"""

import numpy as np
import cv2 as cv
import uuid
import random
from matplotlib.colors import hsv_to_rgb

tmp_filename  = uuid.uuid1().hex + '.mp4'
tmp_filename2 = uuid.uuid1().hex + '.mp4'

cap = cv.VideoCapture(cv.samples.findFile("/labeled/4.hevc"))
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# print(frame1.type)

size        = (frame1.shape[1], frame1.shape[0])
# print(size)
videoWriter = cv.VideoWriter(tmp_filename, cv.VideoWriter_fourcc(*'mp4v'), 20, size)
videoWriter2 = cv.VideoWriter(tmp_filename2, cv.VideoWriter_fourcc(*'mp4v'), 20, size)

prvs = cv.cvtColor(frame1,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)

hsv[...,1] = 255
# hsv[...,2] = 255

mag_thd     = 75

while(ret):
    arrow = np.zeros_like(frame2)

    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        
    mag, ang = cv.cartToPolar(flow[...,0], flow[...,1])
    # hsv[...,0] = ang*180/np.pi/2
    
    hsv[...,0] = cv.normalize(ang*180/np.pi/2,None,0,255,cv.NORM_MINMAX)
    hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
    
    bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
    cv.imshow('frame2',bgr)
    
    # k = cv.waitKey(0) & 0xff
    k = cv.waitKey(1)
    if k == 27:
        break
    # elif k == ord('s'):
    #     print('saved current view ')
    #     # cv.imwrite('opticalfb.png',frame2)
    #     # cv.imwrite('opticalhsv.png',bgr)
    
    videoWriter.write(bgr)
    
    
    mag_fil = np.nonzero(hsv[...,2] > mag_thd)
    for ij in range(len(mag_fil[0])):
        # print(mag_fil[0][ij], ' ', mag_fil[1][ij])
        length =  20*mag[mag_fil[0][ij], mag_fil[1][ij]]
        angle  =  ang[mag_fil[0][ij], mag_fil[1][ij]]
        
        start_pt = (mag_fil[1][ij], mag_fil[0][ij])
        #outward vanishing center
        # end_pt   = (int(mag_fil[1][ij] + length*np.cos(angle)), int(mag_fil[0][ij] + length*np.sin(angle)))
        
        #torward vanishing center
        end_pt   = (int(mag_fil[1][ij] - length*np.cos(angle)), int(mag_fil[0][ij] - length*np.sin(angle)))

        # print(start_pt)
        # print(end_pt)
        
        # r = random.randint(0,255)
        # g = random.randint(0,255)
        # b = random.randint(0,255)
        # rgb = (r,g,b)
        
        hsv_color = hsv[mag_fil[0][ij], mag_fil[1][ij], :]/255
        # rgb_color = tuple(hsv_color)
        rgb_color = hsv_to_rgb(hsv_color)*255
        # rgb_color = cv.cvtColor(hsv_color, cv.COLOR_HSV2RGB)
        
        # print(rgb_color)
        color = (int(rgb_color[0]), int(rgb_color[1]), int(rgb_color[2]))
                
        arrow = cv.line(arrow, start_pt, end_pt, color, thickness=1)
        
    videoWriter2.write(arrow)
    
    
    ret, frame2 = cap.read()
    prvs = next
    
print('print(flow.shape)', flow.shape)
print('mag.shape', mag.shape)

videoWriter.release()
videoWriter2.release()
cv.waitKey(1000)
cv.destroyAllWindows()