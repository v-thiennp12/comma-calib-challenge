 Layer (type)                   Output Shape         Param #     Connected to                     
==================================================================================================
 current_frame (InputLayer)     [(None, 874, 1164,   0           []                               
                                3)]                                                               
                                                                                                  
 previous_frame (InputLayer)    [(None, 874, 1164,   0           []                               
                                3)]                                                               
                                                                                                  
 lambda (Lambda)                (None, 874, 1164, 3  0           ['current_frame[0][0]']          
                                )                                                                 
                                                                                                  
 lambda_1 (Lambda)              (None, 874, 1164, 3  0           ['previous_frame[0][0]']         
                                )                                                                 
                                                                                                  
 conv2d (Conv2D)                (None, 437, 582, 64  9472        ['lambda[0][0]']                 
                                )                                                                 
                                                                                                  
 conv2d_3 (Conv2D)              (None, 437, 582, 64  9472        ['lambda_1[0][0]']               
                                )                                                                 
                                                                                                  
 conv2d_1 (Conv2D)              (None, 219, 291, 12  204928      ['conv2d[0][0]']                 
                                8)                                                                
                                                                                                  
 conv2d_4 (Conv2D)              (None, 219, 291, 12  204928      ['conv2d_3[0][0]']               
                                8)                                                                
                                                                                                  
 conv2d_2 (Conv2D)              (None, 110, 146, 25  819456      ['conv2d_1[0][0]']               
                                6)                                                                
                                                                                                  
 conv2d_5 (Conv2D)              (None, 110, 146, 25  819456      ['conv2d_4[0][0]']               
                                6)                                                                
                                                                                                  
 concatenate (Concatenate)      (None, 220, 146, 25  0           ['conv2d_2[0][0]',               
                                6)                                'conv2d_5[0][0]']               
                                                                                                  
 conv2d_6 (Conv2D)              (None, 220, 146, 25  65792       ['concatenate[0][0]']            
                                6)                                                                
                                                                                                  
 conv2d_7 (Conv2D)              (None, 55, 37, 512)  2097664     ['conv2d_6[0][0]']               
                                                                                                  
 conv2d_8 (Conv2D)              (None, 14, 10, 512)  4194816     ['conv2d_7[0][0]']               
                                                                                                  
 flatten (Flatten)              (None, 71680)        0           ['conv2d_8[0][0]']               
                                                                                                  
 dense (Dense)                  (None, 1)            71681       ['flatten[0][0]']                
                                                                                                  
==================================================================================================
Total params: 8,497,665
Trainable params: 8,497,665
Non-trainable params: 0
__________________________________________________________________________________________________
/home/linhlh12/comma-calib-challenge/model_flownet.py:81: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.
  model.fit_generator(batch_generator_2inputs(data_dir_train, x_train, y_train, batch_size, True),
Epoch 1/15
2021-12-17 19:03:59.848314: I tensorflow/stream_executor/cuda/cuda_dnn.cc:366] Loaded cuDNN version 8301
2021-12-17 19:04:00.210143: I tensorflow/core/platform/default/subprocess.cc:304] Start cannot spawn child process: No such file or directory
250/250 [==============================] - 642s 3s/step - loss: 16.2129 - val_loss: 0.0507
Epoch 2/15
250/250 [==============================] - 637s 3s/step - loss: 0.0048 - val_loss: 0.0553
Epoch 3/15
250/250 [==============================] - 637s 3s/step - loss: 5.1074 - val_loss: 0.7059
Epoch 4/15
250/250 [==============================] - 636s 3s/step - loss: 0.4030 - val_loss: 19.2571
Epoch 5/15
250/250 [==============================] - 637s 3s/step - loss: 3.9434 - val_loss: 1.7404
Epoch 6/15
250/250 [==============================] - 637s 3s/step - loss: 4.1974 - val_loss: 1.1147
Epoch 7/15
250/250 [==============================] - 637s 3s/step - loss: 4.9790 - val_loss: 0.0683
Epoch 8/15
250/250 [==============================] - 637s 3s/step - loss: 2.5025 - val_loss: 0.2458
Epoch 9/15
250/250 [==============================] - 637s 3s/step - loss: 3.5000 - val_loss: 0.1002
Epoch 10/15
250/250 [==============================] - 637s 3s/step - loss: 3.8676 - val_loss: 0.1505
Epoch 11/15
250/250 [==============================] - 637s 3s/step - loss: 3.8210 - val_loss: 6.4775
Epoch 12/15
250/250 [==============================] - 637s 3s/step - loss: 3.6924 - val_loss: 7.8305
Epoch 13/15
250/250 [==============================] - 637s 3s/step - loss: 10.0695 - val_loss: 8.0715
Epoch 14/15
250/250 [==============================] - 636s 3s/step - loss: 0.2672 - val_loss: 0.1199
Epoch 15/15
250/250 [==============================] - 636s 3s/step - loss: 2.0005 - val_loss: 0.8956
Epoch 1/15
250/250 [==============================] - 635s 3s/step - loss: 33.3956 - val_loss: 0.6863
Epoch 2/15
250/250 [==============================] - 634s 3s/step - loss: 0.1245 - val_loss: 0.1421
Epoch 3/15
250/250 [==============================] - 633s 3s/step - loss: 1.9235 - val_loss: 7.2566
Epoch 4/15
250/250 [==============================] - 634s 3s/step - loss: 10.4941 - val_loss: 18.6926
Epoch 5/15
250/250 [==============================] - 632s 3s/step - loss: 70.8579 - val_loss: 0.6279
Epoch 6/15
250/250 [==============================] - 631s 3s/step - loss: 2.2191 - val_loss: 0.5318
Epoch 7/15
250/250 [==============================] - 631s 3s/step - loss: 1.5680 - val_loss: 1.1516
Epoch 8/15
250/250 [==============================] - 632s 3s/step - loss: 2.0546 - val_loss: 2.7835
Epoch 9/15
250/250 [==============================] - 631s 3s/step - loss: 6.3352 - val_loss: 0.3128
Epoch 10/15
250/250 [==============================] - 631s 3s/step - loss: 3.7954 - val_loss: 2.6885
Epoch 11/15
250/250 [==============================] - 631s 3s/step - loss: 12.7896 - val_loss: 25.0484
Epoch 12/15
250/250 [==============================] - 631s 3s/step - loss: 6.4434 - val_loss: 0.4749
Epoch 13/15
250/250 [==============================] - 631s 3s/step - loss: 5.1611 - val_loss: 0.7357
Epoch 14/15
250/250 [==============================] - 632s 3s/step - loss: 10.8057 - val_loss: 9.8287
Epoch 15/15
250/250 [==============================] - 631s 3s/step - loss: 7.1770 - val_loss: 20.8431
Epoch 1/15
250/250 [==============================] - 631s 3s/step - loss: 72.3663 - val_loss: 0.2151
Epoch 2/15
250/250 [==============================] - 631s 3s/step - loss: 0.0951 - val_loss: 0.2113
Epoch 3/15
250/250 [==============================] - 631s 3s/step - loss: 0.0647 - val_loss: 0.2643
Epoch 4/15
250/250 [==============================] - 631s 3s/step - loss: 0.0551 - val_loss: 0.1895
Epoch 5/15
250/250 [==============================] - 631s 3s/step - loss: 0.0969 - val_loss: 0.2602
Epoch 6/15
250/250 [==============================] - 631s 3s/step - loss: 0.1408 - val_loss: 0.2832
Epoch 7/15
250/250 [==============================] - 630s 3s/step - loss: 0.9767 - val_loss: 0.2645
Epoch 8/15
250/250 [==============================] - 631s 3s/step - loss: 9.7183 - val_loss: 6.0638
Epoch 9/15
250/250 [==============================] - 631s 3s/step - loss: 3.1760 - val_loss: 0.7261
Epoch 10/15
250/250 [==============================] - 631s 3s/step - loss: 2.1146 - val_loss: 0.1355
Epoch 11/15
250/250 [==============================] - 632s 3s/step - loss: 5.3292 - val_loss: 1.2371
Epoch 12/15
250/250 [==============================] - 631s 3s/step - loss: 4.0191 - val_loss: 0.6450
Epoch 13/15
250/250 [==============================] - 631s 3s/step - loss: 2.8672 - val_loss: 0.6538
Epoch 14/15
250/250 [==============================] - 631s 3s/step - loss: 3.8706 - val_loss: 1.5673
Epoch 15/15
250/250 [==============================] - 631s 3s/step - loss: 6.0933 - val_loss: 0.9437
Epoch 1/15
250/250 [==============================] - 630s 3s/step - loss: 44.8291 - val_loss: 0.3133
Epoch 2/15
250/250 [==============================] - 631s 3s/step - loss: 0.4639 - val_loss: 1.0348
Epoch 3/15
250/250 [==============================] - 631s 3s/step - loss: 0.6781 - val_loss: 7.4417
Epoch 4/15
250/250 [==============================] - 630s 3s/step - loss: 3.2762 - val_loss: 1.8515
Epoch 5/15
250/250 [==============================] - 631s 3s/step - loss: 7.1157 - val_loss: 5.5262
Epoch 6/15
250/250 [==============================] - 631s 3s/step - loss: 9.3069 - val_loss: 6.6822
Epoch 7/15
250/250 [==============================] - 631s 3s/step - loss: 191.0444 - val_loss: 8129.3804
Epoch 8/15
250/250 [==============================] - 631s 3s/step - loss: 107.8434 - val_loss: 1368.6703
Epoch 9/15
250/250 [==============================] - 631s 3s/step - loss: 1.1254 - val_loss: 1277.5758
Epoch 10/15
250/250 [==============================] - 631s 3s/step - loss: 0.4124 - val_loss: 1264.6000
Epoch 11/15
250/250 [==============================] - 631s 3s/step - loss: 0.2478 - val_loss: 1199.2188
Epoch 12/15
250/250 [==============================] - 631s 3s/step - loss: 0.1919 - val_loss: 1231.6173
Epoch 13/15
250/250 [==============================] - 631s 3s/step - loss: 0.0908 - val_loss: 1182.2568
Epoch 14/15
250/250 [==============================] - 631s 3s/step - loss: 0.0885 - val_loss: 1192.1301
Epoch 15/15
250/250 [==============================] - 631s 3s/step - loss: 0.1320 - val_loss: 1162.2487