51/51 [==============================] - 18s 298ms/step - loss: 6.8506e-04
labeled/4
['loss']
0.0006850555073469877
51/51 [==============================] - 21s 406ms/step - loss: 8.1502e-04
labeled/3
['loss']
0.0008150230278261006
51/51 [==============================] - 20s 394ms/step - loss: 1.6702e-04
labeled/2
['loss']
0.00016701729327905923
51/51 [==============================] - 21s 421ms/step - loss: 2.0772e-04
labeled/1
['loss']
0.0002077200188068673
51/51 [==============================] - 21s 418ms/step - loss: 3.0152e-04
labeled/0
['loss']
0.00030151536338962615

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
    out_concat      = Concatenate(axis=1)([layer_a, layer_b])

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
    model       = Model([in_a, in_b], dense, name="Resnet_mod_regression")
    model.summary()
    plot_model(model, "./Resnet_mod_regression.png", show_shapes=True)    
    return model

def train_model(model, data_dir_train, data_dir_test, x_train, x_valid, y_train, y_valid):
    """
    Train the model
    # """

    epochs              = 15
    samples_per_epoch   = 250  #1000
    batch_size          = 15   #40
    learning_rate       = 1.0E-5
    
    checkpoint = ModelCheckpoint('model-resnet-mod-{epoch:03d}.h5',
                                 monitor='val_loss',
                                 verbose=0,
                                 save_best_only=True,
                                 mode='auto')

    model.compile(loss='mean_squared_error', optimizer='Adam')

    model.fit_generator(batch_generator_2inputs(data_dir_train, x_train, y_train, batch_size, True),
                samples_per_epoch,
                epochs,
                max_queue_size=1,
                validation_data=batch_generator_2inputs(data_dir_test, x_valid, y_valid, batch_size, False),
                validation_steps=len(x_valid),
                callbacks=[checkpoint],
                verbose=1)

if __name__ == '__main__':
    
    #build nvidia-pilotnet model
    model               = build_model()
    
    data_dir_train      = 'labeled/0'
    data_dir_test       = 'labeled/1'    
    x_train, y_train    = utils.load_csv('labeled','0_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','1_tiff.csv')
    train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)

    data_dir_train      = 'labeled/2'
    data_dir_test       = 'labeled/1'
    x_train, y_train    = utils.load_csv('labeled','2_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','1_tiff.csv')
    train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)

    data_dir_train      = 'labeled/3'
    data_dir_test       = 'labeled/1' 
    x_train, y_train    = utils.load_csv('labeled','3_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','1_tiff.csv')
    train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)

    data_dir_train      = 'labeled/4'
    data_dir_test       = 'labeled/1' 
    x_train, y_train    = utils.load_csv('labeled','4_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','1_tiff.csv')
    train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)

    data_dir_train      = 'labeled/1'
    data_dir_test       = 'labeled/1' 
    x_train, y_train    = utils.load_csv('labeled','1_tiff.csv')     
    x_test, y_test      = utils.load_csv('labeled','1_tiff.csv')
    train_model(model, data_dir_train, data_dir_test, x_train, x_test, y_train, y_test)