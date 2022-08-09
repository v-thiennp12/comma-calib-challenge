_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 lambda (Lambda)             (None, 874, 1164, 6)      0         
                                                                 
 conv2d (Conv2D)             (None, 435, 580, 24)      3624      
                                                                 
 conv2d_1 (Conv2D)           (None, 216, 288, 36)      21636     
                                                                 
 conv2d_2 (Conv2D)           (None, 106, 142, 48)      43248     
                                                                 
 conv2d_3 (Conv2D)           (None, 104, 140, 64)      27712     
                                                                 
 conv2d_4 (Conv2D)           (None, 102, 138, 64)      36928     
                                                                 
 dropout (Dropout)           (None, 102, 138, 64)      0         
                                                                 
 flatten (Flatten)           (None, 900864)            0         
                                                                 
 dense (Dense)               (None, 100)               90086500  
                                                                 
 dense_1 (Dense)             (None, 50)                5050      
                                                                 
 dense_2 (Dense)             (None, 10)                510       
                                                                 
 dense_3 (Dense)             (None, 1)                 11        
                                                                 
=================================================================
Total params: 90,225,219
Trainable params: 90,225,219
Non-trainable params: 0
_________________________________________________________________
/home/linhlh12/comma-calib-challenge/model.py:73: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.
  model.fit_generator(batch_generator(data_dir_train, x_train, y_train, batch_size, True),
Epoch 1/10
2021-12-12 01:35:37.135992: I tensorflow/stream_executor/cuda/cuda_dnn.cc:366] Loaded cuDNN version 8301
2021-12-12 01:35:37.488076: I tensorflow/core/platform/default/subprocess.cc:304] Start cannot spawn child process: No such file or directory
250/250 [==============================] - 688s 3s/step - loss: 1696.3383 - val_loss: 0.5418
Epoch 2/10
250/250 [==============================] - 677s 3s/step - loss: 0.7875 - val_loss: 0.0687
Epoch 3/10
250/250 [==============================] - 678s 3s/step - loss: 0.8063 - val_loss: 0.1571
Epoch 4/10
250/250 [==============================] - 678s 3s/step - loss: 1.1928 - val_loss: 0.0063
Epoch 5/10
250/250 [==============================] - 675s 3s/step - loss: 0.4747 - val_loss: 0.9903
Epoch 6/10
250/250 [==============================] - 677s 3s/step - loss: 0.3923 - val_loss: 0.0011
Epoch 7/10
250/250 [==============================] - 678s 3s/step - loss: 0.5432 - val_loss: 0.1164
Epoch 8/10
250/250 [==============================] - 678s 3s/step - loss: 35433236.0000 - val_loss: 1261.3002
Epoch 9/10
250/250 [==============================] - 683s 3s/step - loss: 6258.8760 - val_loss: 518.4159
Epoch 10/10
250/250 [==============================] - 677s 3s/step - loss: 4219.3330 - val_loss: 212.8425