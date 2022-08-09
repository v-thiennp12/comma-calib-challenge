labeled/4
['loss']
0.00035163885331712663
251/251 [==============================] - 76s 303ms/step - loss: 1.3896e-04
labeled/3
['loss']
0.00013895693700760603
251/251 [==============================] - 77s 305ms/step - loss: 1.1294e-04
labeled/2
['loss']
0.00011294063733657822
251/251 [==============================] - 76s 304ms/step - loss: 9.8184e-04
labeled/1
['loss']
0.0009818417020142078
251/251 [==============================] - 77s 307ms/step - loss: 1.9386e-06
labeled/0
['loss']
1.9386054646020057e-06

Epoch 1/30
250/250 [==============================] - 203s 794ms/step - loss: 0.0013 - val_loss: 0.0217
Epoch 2/30
250/250 [==============================] - 198s 792ms/step - loss: 3.8461e-05 - val_loss: 0.0014
Epoch 3/30
250/250 [==============================] - 195s 780ms/step - loss: 1.3778e-05 - val_loss: 0.0828
Epoch 4/30
250/250 [==============================] - 198s 793ms/step - loss: 6.4637e-06 - val_loss: 0.0011
Epoch 5/30
250/250 [==============================] - 195s 781ms/step - loss: 2.6322e-05 - val_loss: 0.2527
Epoch 6/30
250/250 [==============================] - 195s 781ms/step - loss: 1.9424e-05 - val_loss: 0.0013
Epoch 7/30
250/250 [==============================] - 197s 788ms/step - loss: 1.0787e-05 - val_loss: 4.1005e-04
Epoch 8/30
250/250 [==============================] - 196s 783ms/step - loss: 1.8836e-05 - val_loss: 0.0019
Epoch 9/30
250/250 [==============================] - 195s 781ms/step - loss: 1.2858e-04 - val_loss: 0.0193
Epoch 10/30
250/250 [==============================] - 196s 786ms/step - loss: 5.5859e-05 - val_loss: 7.4428e-04
Epoch 11/30
250/250 [==============================] - 194s 779ms/step - loss: 5.7766e-05 - val_loss: 0.0445
Epoch 12/30
250/250 [==============================] - 194s 779ms/step - loss: 5.4605e-05 - val_loss: 0.0084
Epoch 13/30
250/250 [==============================] - 194s 778ms/step - loss: 1.8230e-04 - val_loss: 1400.4171
Epoch 14/30
250/250 [==============================] - 196s 783ms/step - loss: 1.1414e-04 - val_loss: 0.0037
Epoch 15/30
250/250 [==============================] - 196s 785ms/step - loss: 4.7872e-05 - val_loss: 0.0034
Epoch 16/30
250/250 [==============================] - 195s 782ms/step - loss: 6.4605e-05 - val_loss: 4.6509e-04
Epoch 17/30
250/250 [==============================] - 195s 783ms/step - loss: 5.3451e-05 - val_loss: 0.0022
Epoch 18/30
250/250 [==============================] - 196s 784ms/step - loss: 1.4734e-04 - val_loss: 6.5085e-04
Epoch 19/30
250/250 [==============================] - 196s 784ms/step - loss: 1.4662e-05 - val_loss: 0.0067
Epoch 20/30
250/250 [==============================] - 195s 781ms/step - loss: 1.5608e-04 - val_loss: 0.0011
Epoch 21/30
250/250 [==============================] - 195s 782ms/step - loss: 2.8143e-05 - val_loss: 0.0028
Epoch 22/30
250/250 [==============================] - 195s 780ms/step - loss: 1.9234e-05 - val_loss: 4.7768e-04
Epoch 23/30
250/250 [==============================] - 195s 783ms/step - loss: 5.9537e-05 - val_loss: 6.0567e-04
Epoch 24/30
250/250 [==============================] - 195s 782ms/step - loss: 1.0427e-04 - val_loss: 0.0011
Epoch 25/30
250/250 [==============================] - 195s 782ms/step - loss: 3.1685e-05 - val_loss: 0.0019
Epoch 26/30
250/250 [==============================] - 195s 782ms/step - loss: 4.7110e-04 - val_loss: 0.4068
Epoch 27/30
250/250 [==============================] - 195s 780ms/step - loss: 4.1584e-05 - val_loss: 6.8495e-04
Epoch 28/30
250/250 [==============================] - 196s 784ms/step - loss: 4.0419e-06 - val_loss: 0.0027
Epoch 29/30
250/250 [==============================] - 196s 784ms/step - loss: 3.7892e-06 - val_loss: 0.0017
Epoch 30/30
250/250 [==============================] - 195s 781ms/step - loss: 5.1514e-06 - val_loss: 7.0098e-04


#Load saved model
model                   = keras.models.load_model("model-resnet-mod-2-030.h5")
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

def Residual(layer_in, filters, stride):
    # forward path
    layer  = Conv2D(filters, kernel_size=3, strides=stride, padding ='same', use_bias=False)(layer_in)
    layer  = BatchNormalization()(layer)
    layer  = Activation(activations.relu)(layer)
    layer  = Conv2D(filters, kernel_size=3, strides=1, padding ='same', use_bias=False)(layer)
    layer  = BatchNormalization()(layer)
    
    # skip path
    skip_layer = layer_in
    if stride > 1:
        skip_layer  = Conv2D(filters, kernel_size=1, strides=stride, padding ='same', use_bias=False)(skip_layer)
        skip_layer  = BatchNormalization()(skip_layer)
    
    return Activation(activations.relu)(layer + skip_layer)

def DenseResidual(layer_in, filters, stride):
    # forward path
    layer  = Dense(filters, kernel_size=3, strides=stride, padding ='same', use_bias=False)(layer_in)
    layer  = BatchNormalization()(layer)
    layer  = Activation(activations.relu)(layer)
    layer  = Dense(filters, kernel_size=3, strides=1, padding ='same', use_bias=False)(layer)
    layer  = BatchNormalization()(layer)
    
    # skip path
    skip_layer = layer_in
    if stride > 1:
        skip_layer  = Dense(filters, kernel_size=1, strides=stride, padding ='same', use_bias=False)(skip_layer)
        skip_layer  = BatchNormalization()(skip_layer)
    
    return Activation(activations.relu)(layer + skip_layer)

def build_model():
    """
    Modified NVIDIA model
    """

    # IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 66, 200, 3
    # INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)

    ### 
    #Resnet-34 on each branch
    in_a  = Input(shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3), name = 'current_frame')    
    in_b  = Input(shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3), name = 'previous_frame')

    in_a = Lambda(lambda x: x/127.5-1.0, input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3))(in_a)
    in_b = Lambda(lambda x: x/127.5-1.0, input_shape=(IMAGE_HEIGHT, IMAGE_WIDTH, 3))(in_b)

        #1st stage Conv2D 7x7 + Normalization + MaxPool 3x3
    layer_a              = Conv2D(8, kernel_size=7, strides=2, padding='same', use_bias=False)(in_a)
    layer_a              = BatchNormalization()(layer_a)
    layer_a              = Activation(activations.relu)(layer_a)
    layer_a              = MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same')(layer_a)


    layer_b              = Conv2D(8, kernel_size=7, strides=2, padding='same', use_bias=False)(in_b)
    layer_b              = BatchNormalization()(layer_b)
    layer_b              = Activation(activations.relu)(layer_b)
    layer_b              = MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same')(layer_b)
        #2nd stage Deep network of Residuals
            #when depth (number of feature map) doubled, height and width of feature map are halved 
            #filter depth [64, 64, 64, 128, 128, 128, 128, 256, 256, 256, 256, 256, 256, 512, 512, 512]
    prev_filters         = 8
    # for filters in [64]*3 + [128]*4 + [256]*6 + [512]*3: 
    for filters in [64]*3 + [128]*4 + [256]*6 + [512]*3:
        stride       = 1 if filters == prev_filters else 2
        layer_a      = Residual(layer_a, filters, stride)
        prev_filters = filters

    prev_filters         = 8
    # for filters in [64]*3 + [128]*4 + [256]*6 + [512]*3:
    for filters in [64]*3 + [128]*4 + [256]*6 + [512]*3: 
        stride       = 1 if filters == prev_filters else 2
        layer_b      = Residual(layer_b, filters, stride)
        prev_filters = filters        

        #3rd stage GlobalAveragePool + Flatten + Fully Connected for classification
    # layer_a            = GlobalAveragePooling2D()(layer_a) 
    # layer_a            = Flatten()(layer_a) # ?
    # layer_out_a        = Dense(units=n_classes, activation='softmax')(layer_a)

    # layer_b            = GlobalAveragePooling2D()(layer_b) 
    # layer_b            = Flatten()(layer_b) # ?
    # layer_out_b        = Dense(units=n_classes, activation='softmax')(layer_b)

    ###
    #concat 2 branches a&b
    out_concat          = Concatenate(axis=1)([layer_a, layer_b])

    #resnet-34
        #1st stage Conv2D 7x7 + Normalization + MaxPool 3x3
    out_concat              = Conv2D(32, kernel_size=7, strides=1, padding='same', use_bias=False)(out_concat)
    out_concat              = BatchNormalization()(out_concat)
    out_concat              = Activation(activations.relu)(out_concat)
    out_concat              = MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same')(out_concat)

        #2nd stage Deep network of Residuals
            #when depth (number of feature map) doubled, height and width of feature map are halved 
            #filter depth [64, 64, 64, 128, 128, 128, 128, 256, 256, 256, 256, 256, 256, 512, 512, 512]
    prev_filters        = 32
    for filters in [64]*3 + [128]*4 + [256]*6 + [512]*3: 
        stride          = 1 if filters == prev_filters else 2
        out_concat      = Residual(out_concat, filters, stride)
        prev_filters    = filters
    
        #3rd stage GlobalAveragePool + Flatten + Fully Connected for classification
    out_concat         = BatchNormalization()(out_concat) 
    out_concat         = Activation(activations.relu)(out_concat)
    flatted            = Flatten()(out_concat) # ?
    dense              = Dense(1, activation='linear')(flatted)   

    #
    model       = Model([in_a, in_b], dense, name="Resnet_mod_2_regression")
    model.summary()
    plot_model(model, "./Resnet_mod_2_regression.png", show_shapes=True)    
    return model

def train_model(model, data_dir_train, data_dir_test, x_train, x_valid, y_train, y_valid):
    """
    Train the model
    # """

    epochs              = 30
    samples_per_epoch   = 250  #1000
    batch_size          = 15   #40
    learning_rate       = 1.0E-5
    
    checkpoint = ModelCheckpoint('model-resnet-mod-2-{epoch:03d}.h5',
                                 monitor='val_loss',
                                 verbose=0,
                                 save_best_only=True,
                                 mode='auto')

    model.compile(loss='mean_squared_error', optimizer='Adam')

    model.fit_generator(batch_generator_2inputs(data_dir_train, x_train, y_train, batch_size, True),
                samples_per_epoch,
                epochs,
                max_queue_size=1,
                validation_data=batch_generator_2inputs(data_dir_train, x_train, y_train, batch_size, False),
                validation_steps=samples_per_epoch, #len(x_valid),
                callbacks=[checkpoint],
                verbose=1)

if __name__ == '__main__':
    
    #build nvidia-pilotnet model
    model               = build_model()
    
    data_dir_train      = 'labeled/0'
    data_dir_test       = 'labeled/4'    
    x_train, y_train    = utils.load_csv('labeled','0_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','4_tiff.csv')
    train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)

    data_dir_train      = 'labeled/2'
    data_dir_test       = 'labeled/4'
    x_train, y_train    = utils.load_csv('labeled','2_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','4_tiff.csv')
    train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)

    data_dir_train      = 'labeled/3'
    data_dir_test       = 'labeled/4' 
    x_train, y_train    = utils.load_csv('labeled','3_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','4_tiff.csv')
    train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)

    # data_dir_train      = 'labeled/4'
    # data_dir_test       = 'labeled/1' 
    # x_train, y_train    = utils.load_csv('labeled','4_tiff.csv')     
    # x_test, y_test      = utils.load_csv('labeled','1_tiff.csv')
    # train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)

    data_dir_train      = 'labeled/1'
    data_dir_test       = 'labeled/4' 
    x_train, y_train    = utils.load_csv('labeled','1_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','4_tiff.csv')
    train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)

Epoch 13/30
250/250 [==============================] - 196s 786ms/step - loss: 3.6839e-04 - val_loss: 4.6578e-04
Epoch 14/30
250/250 [==============================] - 194s 779ms/step - loss: 0.0011 - val_loss: 0.0264
Epoch 15/30
250/250 [==============================] - 195s 783ms/step - loss: 0.0014 - val_loss: 0.0025
Epoch 16/30
250/250 [==============================] - 194s 779ms/step - loss: 0.0029 - val_loss: 0.0136
Epoch 17/30
250/250 [==============================] - 195s 783ms/step - loss: 8.1347e-04 - val_loss: 9.5172e-04
Epoch 18/30
250/250 [==============================] - 195s 782ms/step - loss: 0.0061 - val_loss: 0.0018
Epoch 19/30
250/250 [==============================] - 195s 783ms/step - loss: 3.7581e-04 - val_loss: 0.0011
Epoch 20/30
250/250 [==============================] - 196s 785ms/step - loss: 8.1419e-04 - val_loss: 3.8607e-04
Epoch 21/30
250/250 [==============================] - 196s 785ms/step - loss: 9.3764e-05 - val_loss: 3.2456e-04
Epoch 22/30
250/250 [==============================] - 194s 778ms/step - loss: 1.6591e-04 - val_loss: 8.5666e-04
Epoch 23/30
250/250 [==============================] - 195s 779ms/step - loss: 1.5055e-04 - val_loss: 0.0021
Epoch 24/30
250/250 [==============================] - 195s 783ms/step - loss: 2.3582e-04 - val_loss: 8.1426e-04
Epoch 25/30
250/250 [==============================] - 195s 781ms/step - loss: 4.3165e-04 - val_loss: 6.3110e-04
Epoch 26/30
250/250 [==============================] - 196s 784ms/step - loss: 5.9883e-04 - val_loss: 0.0054
Epoch 27/30
250/250 [==============================] - 195s 781ms/step - loss: 4.9472e-04 - val_loss: 6.8319e-04
Epoch 28/30
250/250 [==============================] - 194s 778ms/step - loss: 1.9772e-04 - val_loss: 0.0025
Epoch 29/30
250/250 [==============================] - 195s 781ms/step - loss: 9.1272e-04 - val_loss: 0.0183
Epoch 30/30
250/250 [==============================] - 194s 779ms/step - loss: 0.0012 - val_loss: 0.0013
Epoch 1/30
250/250 [==============================] - 203s 796ms/step - loss: 0.0064 - val_loss: 0.1138
Epoch 2/30
250/250 [==============================] - 196s 784ms/step - loss: 5.6905e-04 - val_loss: 141.7739
Epoch 3/30
250/250 [==============================] - 198s 794ms/step - loss: 5.1445e-04 - val_loss: 8.5973e-04
Epoch 4/30
250/250 [==============================] - 880s 4s/step - loss: 6.3189e-04 - val_loss: 0.0274
Epoch 5/30
250/250 [==============================] - 195s 780ms/step - loss: 1.6190e-04 - val_loss: 0.0187
Epoch 6/30
250/250 [==============================] - 195s 780ms/step - loss: 1.4283e-04 - val_loss: 0.1378
Epoch 7/30
250/250 [==============================] - 194s 778ms/step - loss: 2.8923e-04 - val_loss: 0.0015
Epoch 8/30
250/250 [==============================] - 195s 779ms/step - loss: 1.8925e-04 - val_loss: 0.1208
Epoch 9/30
250/250 [==============================] - 195s 782ms/step - loss: 4.5176e-04 - val_loss: 0.0018
Epoch 10/30
250/250 [==============================] - 195s 781ms/step - loss: 2.1245e-04 - val_loss: 0.0038
Epoch 11/30
250/250 [==============================] - 196s 784ms/step - loss: 2.0593e-04 - val_loss: 0.0451
Epoch 12/30
250/250 [==============================] - 195s 780ms/step - loss: 2.5417e-04 - val_loss: 0.0266
Epoch 13/30
250/250 [==============================] - 195s 781ms/step - loss: 4.5955e-04 - val_loss: 0.0029
Epoch 14/30
250/250 [==============================] - 195s 783ms/step - loss: 0.0056 - val_loss: 97.5400
Epoch 15/30
250/250 [==============================] - 196s 786ms/step - loss: 2.1190e-04 - val_loss: 0.0470
Epoch 16/30
250/250 [==============================] - 195s 781ms/step - loss: 1.0645e-04 - val_loss: 0.0038
Epoch 17/30
250/250 [==============================] - 194s 779ms/step - loss: 1.0431e-04 - val_loss: 0.0079
Epoch 18/30
250/250 [==============================] - 194s 777ms/step - loss: 1.6047e-04 - val_loss: 0.0016
Epoch 19/30
250/250 [==============================] - 195s 781ms/step - loss: 1.6800e-04 - val_loss: 0.0033
Epoch 20/30
250/250 [==============================] - 195s 782ms/step - loss: 1.0374e-04 - val_loss: 0.0019
Epoch 21/30
250/250 [==============================] - 195s 780ms/step - loss: 1.3864e-04 - val_loss: 0.0012
Epoch 22/30
250/250 [==============================] - 195s 780ms/step - loss: 2.4700e-04 - val_loss: 0.0048
Epoch 23/30
250/250 [==============================] - 195s 780ms/step - loss: 2.4278e-04 - val_loss: 0.0028
Epoch 24/30
250/250 [==============================] - 196s 783ms/step - loss: 2.3528e-04 - val_loss: 0.0014
Epoch 25/30
250/250 [==============================] - 194s 776ms/step - loss: 3.9265e-04 - val_loss: 0.0011
Epoch 26/30
250/250 [==============================] - 196s 787ms/step - loss: 7.2055e-04 - val_loss: 7.4000e-04
Epoch 27/30
250/250 [==============================] - 197s 788ms/step - loss: 1.7540e-04 - val_loss: 4.9404e-04
Epoch 28/30
250/250 [==============================] - 196s 783ms/step - loss: 1.6150e-04 - val_loss: 2.4731e-04
Epoch 29/30
250/250 [==============================] - 195s 783ms/step - loss: 1.4998e-04 - val_loss: 0.0027
Epoch 30/30
250/250 [==============================] - 194s 779ms/step - loss: 2.1211e-04 - val_loss: 1.0729e-04
Epoch 1/30
250/250 [==============================] - 202s 790ms/step - loss: 0.0013 - val_loss: 0.0066
Epoch 2/30
250/250 [==============================] - 196s 784ms/step - loss: 6.1354e-05 - val_loss: 0.0100
Epoch 3/30
250/250 [==============================] - 194s 776ms/step - loss: 1.4261e-04 - val_loss: 508.5496
Epoch 4/30
250/250 [==============================] - 198s 793ms/step - loss: 7.3355e-05 - val_loss: 0.0060
Epoch 5/30
250/250 [==============================] - 194s 776ms/step - loss: 2.8001e-04 - val_loss: 0.0086
Epoch 6/30
250/250 [==============================] - 195s 781ms/step - loss: 1.2206e-04 - val_loss: 0.3132
Epoch 7/30
250/250 [==============================] - 196s 786ms/step - loss: 1.6150e-04 - val_loss: 0.0060
Epoch 8/30
250/250 [==============================] - 195s 780ms/step - loss: 1.5120e-04 - val_loss: 0.0017
Epoch 9/30
250/250 [==============================] - 196s 785ms/step - loss: 2.1755e-04 - val_loss: 0.0016
Epoch 10/30
250/250 [==============================] - 195s 780ms/step - loss: 2.2325e-04 - val_loss: 2.6452e-04
Epoch 11/30
250/250 [==============================] - 195s 783ms/step - loss: 2.1573e-04 - val_loss: 3.3752e-05
Epoch 12/30
250/250 [==============================] - 195s 781ms/step - loss: 2.0973e-04 - val_loss: 0.0019
Epoch 13/30
250/250 [==============================] - 195s 781ms/step - loss: 1.1918e-04 - val_loss: 0.0058
Epoch 14/30
250/250 [==============================] - 195s 781ms/step - loss: 2.2490e-04 - val_loss: 0.0075
Epoch 15/30
250/250 [==============================] - 195s 780ms/step - loss: 1.5091e-04 - val_loss: 0.0016
Epoch 16/30
250/250 [==============================] - 196s 784ms/step - loss: 8.5928e-05 - val_loss: 2.7619e-04
Epoch 17/30
250/250 [==============================] - 195s 782ms/step - loss: 1.2822e-04 - val_loss: 0.1589
Epoch 18/30
250/250 [==============================] - 195s 781ms/step - loss: 1.3606e-04 - val_loss: 1.9489e-04
Epoch 19/30
250/250 [==============================] - 196s 783ms/step - loss: 8.4141e-05 - val_loss: 0.0223
Epoch 20/30
250/250 [==============================] - 195s 782ms/step - loss: 1.0983e-04 - val_loss: 0.0011
Epoch 21/30
250/250 [==============================] - 195s 782ms/step - loss: 1.2187e-04 - val_loss: 0.0038
Epoch 22/30
250/250 [==============================] - 195s 781ms/step - loss: 7.7774e-05 - val_loss: 0.0169
Epoch 23/30
250/250 [==============================] - 195s 782ms/step - loss: 2.8255e-04 - val_loss: 0.0144
Epoch 24/30
250/250 [==============================] - 196s 785ms/step - loss: 8.4134e-05 - val_loss: 0.0021
Epoch 25/30
250/250 [==============================] - 194s 779ms/step - loss: 7.1745e-05 - val_loss: 0.0033
Epoch 26/30
250/250 [==============================] - 196s 784ms/step - loss: 3.3196e-04 - val_loss: 0.0026
Epoch 27/30
250/250 [==============================] - 195s 782ms/step - loss: 1.0958e-04 - val_loss: 9.8922e-04
Epoch 28/30
250/250 [==============================] - 195s 780ms/step - loss: 7.7618e-05 - val_loss: 0.0014
Epoch 29/30
250/250 [==============================] - 196s 784ms/step - loss: 9.9623e-05 - val_loss: 0.0073
Epoch 30/30
250/250 [==============================] - 195s 781ms/step - loss: 1.9700e-04 - val_loss: 5.6621e-04
Epoch 1/30
250/250 [==============================] - 203s 794ms/step - loss: 0.0013 - val_loss: 0.0217
Epoch 2/30
250/250 [==============================] - 198s 792ms/step - loss: 3.8461e-05 - val_loss: 0.0014
Epoch 3/30
250/250 [==============================] - 195s 780ms/step - loss: 1.3778e-05 - val_loss: 0.0828
Epoch 4/30
250/250 [==============================] - 198s 793ms/step - loss: 6.4637e-06 - val_loss: 0.0011
Epoch 5/30
250/250 [==============================] - 195s 781ms/step - loss: 2.6322e-05 - val_loss: 0.2527
Epoch 6/30
250/250 [==============================] - 195s 781ms/step - loss: 1.9424e-05 - val_loss: 0.0013
Epoch 7/30
250/250 [==============================] - 197s 788ms/step - loss: 1.0787e-05 - val_loss: 4.1005e-04
Epoch 8/30
250/250 [==============================] - 196s 783ms/step - loss: 1.8836e-05 - val_loss: 0.0019
Epoch 9/30
250/250 [==============================] - 195s 781ms/step - loss: 1.2858e-04 - val_loss: 0.0193
Epoch 10/30
250/250 [==============================] - 196s 786ms/step - loss: 5.5859e-05 - val_loss: 7.4428e-04
Epoch 11/30
250/250 [==============================] - 194s 779ms/step - loss: 5.7766e-05 - val_loss: 0.0445
Epoch 12/30
250/250 [==============================] - 194s 779ms/step - loss: 5.4605e-05 - val_loss: 0.0084
Epoch 13/30
250/250 [==============================] - 194s 778ms/step - loss: 1.8230e-04 - val_loss: 1400.4171
Epoch 14/30
250/250 [==============================] - 196s 783ms/step - loss: 1.1414e-04 - val_loss: 0.0037
Epoch 15/30
250/250 [==============================] - 196s 785ms/step - loss: 4.7872e-05 - val_loss: 0.0034
Epoch 16/30
250/250 [==============================] - 195s 782ms/step - loss: 6.4605e-05 - val_loss: 4.6509e-04
Epoch 17/30
250/250 [==============================] - 195s 783ms/step - loss: 5.3451e-05 - val_loss: 0.0022
Epoch 18/30
250/250 [==============================] - 196s 784ms/step - loss: 1.4734e-04 - val_loss: 6.5085e-04
Epoch 19/30
250/250 [==============================] - 196s 784ms/step - loss: 1.4662e-05 - val_loss: 0.0067
Epoch 20/30
250/250 [==============================] - 195s 781ms/step - loss: 1.5608e-04 - val_loss: 0.0011
Epoch 21/30
250/250 [==============================] - 195s 782ms/step - loss: 2.8143e-05 - val_loss: 0.0028
Epoch 22/30
250/250 [==============================] - 195s 780ms/step - loss: 1.9234e-05 - val_loss: 4.7768e-04
Epoch 23/30
250/250 [==============================] - 195s 783ms/step - loss: 5.9537e-05 - val_loss: 6.0567e-04
Epoch 24/30
250/250 [==============================] - 195s 782ms/step - loss: 1.0427e-04 - val_loss: 0.0011
Epoch 25/30
250/250 [==============================] - 195s 782ms/step - loss: 3.1685e-05 - val_loss: 0.0019
Epoch 26/30
250/250 [==============================] - 195s 782ms/step - loss: 4.7110e-04 - val_loss: 0.4068
Epoch 27/30
250/250 [==============================] - 195s 780ms/step - loss: 4.1584e-05 - val_loss: 6.8495e-04
Epoch 28/30
250/250 [==============================] - 196s 784ms/step - loss: 4.0419e-06 - val_loss: 0.0027
Epoch 29/30
250/250 [==============================] - 196s 784ms/step - loss: 3.7892e-06 - val_loss: 0.0017
Epoch 30/30
250/250 [==============================] - 195s 781ms/step - loss: 5.1514e-06 - val_loss: 7.0098e-04