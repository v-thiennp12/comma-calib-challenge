Activation_38 (Activation)     (None, 219, 291, 32  0           ['batch_normalization_39[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_7 (Conv2D)              (None, 219, 291, 32  9216        ['activation_6[1][0]']           
                                )                                                                 
                                                                                                  
 conv2d_40 (Conv2D)             (None, 219, 291, 32  9216        ['activation_38[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_7 (BatchNo  (None, 219, 291, 32  128        ['conv2d_7[1][0]']               
 rmalization)                   )                                                                 
                                                                                                  
 batch_normalization_40 (BatchN  (None, 219, 291, 32  128        ['conv2d_40[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_2 (TFOpLa  (None, 219, 291, 32  0          ['batch_normalization_7[1][0]',  
 mbda)                          )                                 'activation_5[1][0]']           
                                                                                                  
 tf.__operators__.add_18 (TFOpL  (None, 219, 291, 32  0          ['batch_normalization_40[1][0]', 
 ambda)                         )                                 'activation_37[1][0]']          
                                                                                                  
 activation_7 (Activation)      (None, 219, 291, 32  0           ['tf.__operators__.add_2[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_39 (Activation)     (None, 219, 291, 32  0           ['tf.__operators__.add_18[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_8 (Conv2D)              (None, 110, 146, 64  18432       ['activation_7[1][0]']           
                                )                                                                 
                                                                                                  
 conv2d_41 (Conv2D)             (None, 110, 146, 64  18432       ['activation_39[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_8 (BatchNo  (None, 110, 146, 64  256        ['conv2d_8[1][0]']               
 rmalization)                   )                                                                 
                                                                                                  
 batch_normalization_41 (BatchN  (None, 110, 146, 64  256        ['conv2d_41[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_8 (Activation)      (None, 110, 146, 64  0           ['batch_normalization_8[1][0]']  
                                )                                                                 
                                                                                                  
 activation_40 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_41[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_9 (Conv2D)              (None, 110, 146, 64  36864       ['activation_8[1][0]']           
                                )                                                                 
                                                                                                  
 conv2d_10 (Conv2D)             (None, 110, 146, 64  2048        ['activation_7[1][0]']           
                                )                                                                 
                                                                                                  
 conv2d_42 (Conv2D)             (None, 110, 146, 64  36864       ['activation_40[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_43 (Conv2D)             (None, 110, 146, 64  2048        ['activation_39[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_9 (BatchNo  (None, 110, 146, 64  256        ['conv2d_9[1][0]']               
 rmalization)                   )                                                                 
                                                                                                  
 batch_normalization_10 (BatchN  (None, 110, 146, 64  256        ['conv2d_10[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_42 (BatchN  (None, 110, 146, 64  256        ['conv2d_42[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_43 (BatchN  (None, 110, 146, 64  256        ['conv2d_43[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_3 (TFOpLa  (None, 110, 146, 64  0          ['batch_normalization_9[1][0]',  
 mbda)                          )                                 'batch_normalization_10[1][0]'] 
                                                                                                  
 tf.__operators__.add_19 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_42[1][0]', 
 ambda)                         )                                 'batch_normalization_43[1][0]'] 
                                                                                                  
 activation_9 (Activation)      (None, 110, 146, 64  0           ['tf.__operators__.add_3[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_41 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_19[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_11 (Conv2D)             (None, 110, 146, 64  36864       ['activation_9[1][0]']           
                                )                                                                 
                                                                                                  
 conv2d_44 (Conv2D)             (None, 110, 146, 64  36864       ['activation_41[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_11 (BatchN  (None, 110, 146, 64  256        ['conv2d_11[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_44 (BatchN  (None, 110, 146, 64  256        ['conv2d_44[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_10 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_11[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_42 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_44[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_12 (Conv2D)             (None, 110, 146, 64  36864       ['activation_10[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_45 (Conv2D)             (None, 110, 146, 64  36864       ['activation_42[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_12 (BatchN  (None, 110, 146, 64  256        ['conv2d_12[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_45 (BatchN  (None, 110, 146, 64  256        ['conv2d_45[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_4 (TFOpLa  (None, 110, 146, 64  0          ['batch_normalization_12[1][0]', 
 mbda)                          )                                 'activation_9[1][0]']           
                                                                                                  
 tf.__operators__.add_20 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_45[1][0]', 
 ambda)                         )                                 'activation_41[1][0]']          
                                                                                                  
 activation_11 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_4[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_43 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_20[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_13 (Conv2D)             (None, 110, 146, 64  36864       ['activation_11[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_46 (Conv2D)             (None, 110, 146, 64  36864       ['activation_43[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_13 (BatchN  (None, 110, 146, 64  256        ['conv2d_13[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_46 (BatchN  (None, 110, 146, 64  256        ['conv2d_46[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_12 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_13[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_44 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_46[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_14 (Conv2D)             (None, 110, 146, 64  36864       ['activation_12[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_47 (Conv2D)             (None, 110, 146, 64  36864       ['activation_44[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_14 (BatchN  (None, 110, 146, 64  256        ['conv2d_14[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_47 (BatchN  (None, 110, 146, 64  256        ['conv2d_47[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_5 (TFOpLa  (None, 110, 146, 64  0          ['batch_normalization_14[1][0]', 
 mbda)                          )                                 'activation_11[1][0]']          
                                                                                                  
 tf.__operators__.add_21 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_47[1][0]', 
 ambda)                         )                                 'activation_43[1][0]']          
                                                                                                  
 activation_13 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_5[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_45 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_21[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_15 (Conv2D)             (None, 110, 146, 64  36864       ['activation_13[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_48 (Conv2D)             (None, 110, 146, 64  36864       ['activation_45[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_15 (BatchN  (None, 110, 146, 64  256        ['conv2d_15[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_48 (BatchN  (None, 110, 146, 64  256        ['conv2d_48[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_14 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_15[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_46 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_48[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_16 (Conv2D)             (None, 110, 146, 64  36864       ['activation_14[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_49 (Conv2D)             (None, 110, 146, 64  36864       ['activation_46[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_16 (BatchN  (None, 110, 146, 64  256        ['conv2d_16[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_49 (BatchN  (None, 110, 146, 64  256        ['conv2d_49[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_6 (TFOpLa  (None, 110, 146, 64  0          ['batch_normalization_16[1][0]', 
 mbda)                          )                                 'activation_13[1][0]']          
                                                                                                  
 tf.__operators__.add_22 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_49[1][0]', 
 ambda)                         )                                 'activation_45[1][0]']          
                                                                                                  
 activation_15 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_6[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_47 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_22[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_17 (Conv2D)             (None, 110, 146, 64  36864       ['activation_15[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_50 (Conv2D)             (None, 110, 146, 64  36864       ['activation_47[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_17 (BatchN  (None, 110, 146, 64  256        ['conv2d_17[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_50 (BatchN  (None, 110, 146, 64  256        ['conv2d_50[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_16 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_17[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_48 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_50[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_18 (Conv2D)             (None, 110, 146, 64  36864       ['activation_16[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_51 (Conv2D)             (None, 110, 146, 64  36864       ['activation_48[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_18 (BatchN  (None, 110, 146, 64  256        ['conv2d_18[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_51 (BatchN  (None, 110, 146, 64  256        ['conv2d_51[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_7 (TFOpLa  (None, 110, 146, 64  0          ['batch_normalization_18[1][0]', 
 mbda)                          )                                 'activation_15[1][0]']          
                                                                                                  
 tf.__operators__.add_23 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_51[1][0]', 
 ambda)                         )                                 'activation_47[1][0]']          
                                                                                                  
 activation_17 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_7[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_49 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_23[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_19 (Conv2D)             (None, 110, 146, 64  36864       ['activation_17[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_52 (Conv2D)             (None, 110, 146, 64  36864       ['activation_49[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_19 (BatchN  (None, 110, 146, 64  256        ['conv2d_19[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_52 (BatchN  (None, 110, 146, 64  256        ['conv2d_52[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_18 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_19[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_50 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_52[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_20 (Conv2D)             (None, 110, 146, 64  36864       ['activation_18[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_53 (Conv2D)             (None, 110, 146, 64  36864       ['activation_50[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_20 (BatchN  (None, 110, 146, 64  256        ['conv2d_20[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_53 (BatchN  (None, 110, 146, 64  256        ['conv2d_53[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_8 (TFOpLa  (None, 110, 146, 64  0          ['batch_normalization_20[1][0]', 
 mbda)                          )                                 'activation_17[1][0]']          
                                                                                                  
 tf.__operators__.add_24 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_53[1][0]', 
 ambda)                         )                                 'activation_49[1][0]']          
                                                                                                  
 activation_19 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_8[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_51 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_24[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_21 (Conv2D)             (None, 110, 146, 64  36864       ['activation_19[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_54 (Conv2D)             (None, 110, 146, 64  36864       ['activation_51[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_21 (BatchN  (None, 110, 146, 64  256        ['conv2d_21[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_54 (BatchN  (None, 110, 146, 64  256        ['conv2d_54[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_20 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_21[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_52 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_54[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_22 (Conv2D)             (None, 110, 146, 64  36864       ['activation_20[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_55 (Conv2D)             (None, 110, 146, 64  36864       ['activation_52[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_22 (BatchN  (None, 110, 146, 64  256        ['conv2d_22[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_55 (BatchN  (None, 110, 146, 64  256        ['conv2d_55[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_9 (TFOpLa  (None, 110, 146, 64  0          ['batch_normalization_22[1][0]', 
 mbda)                          )                                 'activation_19[1][0]']          
                                                                                                  
 tf.__operators__.add_25 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_55[1][0]', 
 ambda)                         )                                 'activation_51[1][0]']          
                                                                                                  
 activation_21 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_9[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_53 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_25[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_23 (Conv2D)             (None, 110, 146, 64  36864       ['activation_21[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_56 (Conv2D)             (None, 110, 146, 64  36864       ['activation_53[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_23 (BatchN  (None, 110, 146, 64  256        ['conv2d_23[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_56 (BatchN  (None, 110, 146, 64  256        ['conv2d_56[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_22 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_23[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_54 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_56[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_24 (Conv2D)             (None, 110, 146, 64  36864       ['activation_22[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_57 (Conv2D)             (None, 110, 146, 64  36864       ['activation_54[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_24 (BatchN  (None, 110, 146, 64  256        ['conv2d_24[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_57 (BatchN  (None, 110, 146, 64  256        ['conv2d_57[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_10 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_24[1][0]', 
 ambda)                         )                                 'activation_21[1][0]']          
                                                                                                  
 tf.__operators__.add_26 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_57[1][0]', 
 ambda)                         )                                 'activation_53[1][0]']          
                                                                                                  
 activation_23 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_10[1][0]']
                                )                                                                 
                                                                                                  
 activation_55 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_26[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_25 (Conv2D)             (None, 110, 146, 64  36864       ['activation_23[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_58 (Conv2D)             (None, 110, 146, 64  36864       ['activation_55[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_25 (BatchN  (None, 110, 146, 64  256        ['conv2d_25[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_58 (BatchN  (None, 110, 146, 64  256        ['conv2d_58[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_24 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_25[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_56 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_58[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_26 (Conv2D)             (None, 110, 146, 64  36864       ['activation_24[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_59 (Conv2D)             (None, 110, 146, 64  36864       ['activation_56[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_26 (BatchN  (None, 110, 146, 64  256        ['conv2d_26[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_59 (BatchN  (None, 110, 146, 64  256        ['conv2d_59[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_11 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_26[1][0]', 
 ambda)                         )                                 'activation_23[1][0]']          
                                                                                                  
 tf.__operators__.add_27 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_59[1][0]', 
 ambda)                         )                                 'activation_55[1][0]']          
                                                                                                  
 activation_25 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_11[1][0]']
                                )                                                                 
                                                                                                  
 activation_57 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_27[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_27 (Conv2D)             (None, 110, 146, 64  36864       ['activation_25[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_60 (Conv2D)             (None, 110, 146, 64  36864       ['activation_57[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_27 (BatchN  (None, 110, 146, 64  256        ['conv2d_27[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_60 (BatchN  (None, 110, 146, 64  256        ['conv2d_60[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_26 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_27[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_58 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_60[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_28 (Conv2D)             (None, 110, 146, 64  36864       ['activation_26[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_61 (Conv2D)             (None, 110, 146, 64  36864       ['activation_58[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_28 (BatchN  (None, 110, 146, 64  256        ['conv2d_28[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_61 (BatchN  (None, 110, 146, 64  256        ['conv2d_61[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_12 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_28[1][0]', 
 ambda)                         )                                 'activation_25[1][0]']          
                                                                                                  
 tf.__operators__.add_28 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_61[1][0]', 
 ambda)                         )                                 'activation_57[1][0]']          
                                                                                                  
 activation_27 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_12[1][0]']
                                )                                                                 
                                                                                                  
 activation_59 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_28[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_29 (Conv2D)             (None, 110, 146, 64  36864       ['activation_27[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_62 (Conv2D)             (None, 110, 146, 64  36864       ['activation_59[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_29 (BatchN  (None, 110, 146, 64  256        ['conv2d_29[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_62 (BatchN  (None, 110, 146, 64  256        ['conv2d_62[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_28 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_29[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_60 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_62[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_30 (Conv2D)             (None, 110, 146, 64  36864       ['activation_28[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_63 (Conv2D)             (None, 110, 146, 64  36864       ['activation_60[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_30 (BatchN  (None, 110, 146, 64  256        ['conv2d_30[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_63 (BatchN  (None, 110, 146, 64  256        ['conv2d_63[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_13 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_30[1][0]', 
 ambda)                         )                                 'activation_27[1][0]']          
                                                                                                  
 tf.__operators__.add_29 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_63[1][0]', 
 ambda)                         )                                 'activation_59[1][0]']          
                                                                                                  
 activation_29 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_13[1][0]']
                                )                                                                 
                                                                                                  
 activation_61 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_29[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_31 (Conv2D)             (None, 110, 146, 64  36864       ['activation_29[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_64 (Conv2D)             (None, 110, 146, 64  36864       ['activation_61[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_31 (BatchN  (None, 110, 146, 64  256        ['conv2d_31[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_64 (BatchN  (None, 110, 146, 64  256        ['conv2d_64[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_30 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_31[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_62 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_64[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_32 (Conv2D)             (None, 110, 146, 64  36864       ['activation_30[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_65 (Conv2D)             (None, 110, 146, 64  36864       ['activation_62[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_32 (BatchN  (None, 110, 146, 64  256        ['conv2d_32[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_65 (BatchN  (None, 110, 146, 64  256        ['conv2d_65[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_14 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_32[1][0]', 
 ambda)                         )                                 'activation_29[1][0]']          
                                                                                                  
 tf.__operators__.add_30 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_65[1][0]', 
 ambda)                         )                                 'activation_61[1][0]']          
                                                                                                  
 activation_31 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_14[1][0]']
                                )                                                                 
                                                                                                  
 activation_63 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_30[1][0]']
                                )                                                                 
                                                                                                  
 conv2d_33 (Conv2D)             (None, 110, 146, 64  36864       ['activation_31[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_66 (Conv2D)             (None, 110, 146, 64  36864       ['activation_63[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_33 (BatchN  (None, 110, 146, 64  256        ['conv2d_33[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_66 (BatchN  (None, 110, 146, 64  256        ['conv2d_66[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 activation_32 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_33[1][0]'] 
                                )                                                                 
                                                                                                  
 activation_64 (Activation)     (None, 110, 146, 64  0           ['batch_normalization_66[1][0]'] 
                                )                                                                 
                                                                                                  
 conv2d_34 (Conv2D)             (None, 110, 146, 64  36864       ['activation_32[1][0]']          
                                )                                                                 
                                                                                                  
 conv2d_67 (Conv2D)             (None, 110, 146, 64  36864       ['activation_64[1][0]']          
                                )                                                                 
                                                                                                  
 batch_normalization_34 (BatchN  (None, 110, 146, 64  256        ['conv2d_34[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 batch_normalization_67 (BatchN  (None, 110, 146, 64  256        ['conv2d_67[1][0]']              
 ormalization)                  )                                                                 
                                                                                                  
 tf.__operators__.add_15 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_34[1][0]', 
 ambda)                         )                                 'activation_31[1][0]']          
                                                                                                  
 tf.__operators__.add_31 (TFOpL  (None, 110, 146, 64  0          ['batch_normalization_67[1][0]', 
 ambda)                         )                                 'activation_63[1][0]']          
                                                                                                  
 activation_33 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_15[1][0]']
                                )                                                                 
                                                                                                  
 activation_65 (Activation)     (None, 110, 146, 64  0           ['tf.__operators__.add_31[1][0]']
                                )                                                                 
                                                                                                  
 concatenate (Concatenate)      (None, 220, 146, 64  0           ['activation_33[1][0]',          
                                )                                 'activation_65[1][0]']          
                                                                                                  
 conv2d_68 (Conv2D)             (None, 110, 73, 32)  100352      ['concatenate[1][0]']            
                                                                                                  
 batch_normalization_68 (BatchN  (None, 110, 73, 32)  128        ['conv2d_68[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_66 (Activation)     (None, 110, 73, 32)  0           ['batch_normalization_68[1][0]'] 
                                                                                                  
 max_pooling2d_2 (MaxPooling2D)  (None, 55, 37, 32)  0           ['activation_66[1][0]']          
                                                                                                  
 conv2d_69 (Conv2D)             (None, 55, 37, 32)   9216        ['max_pooling2d_2[1][0]']        
                                                                                                  
 batch_normalization_69 (BatchN  (None, 55, 37, 32)  128         ['conv2d_69[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_67 (Activation)     (None, 55, 37, 32)   0           ['batch_normalization_69[1][0]'] 
                                                                                                  
 conv2d_70 (Conv2D)             (None, 55, 37, 32)   9216        ['activation_67[1][0]']          
                                                                                                  
 batch_normalization_70 (BatchN  (None, 55, 37, 32)  128         ['conv2d_70[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_32 (TFOpL  (None, 55, 37, 32)  0           ['batch_normalization_70[1][0]', 
 ambda)                                                           'max_pooling2d_2[1][0]']        
                                                                                                  
 activation_68 (Activation)     (None, 55, 37, 32)   0           ['tf.__operators__.add_32[1][0]']
                                                                                                  
 conv2d_71 (Conv2D)             (None, 55, 37, 32)   9216        ['activation_68[1][0]']          
                                                                                                  
 batch_normalization_71 (BatchN  (None, 55, 37, 32)  128         ['conv2d_71[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_69 (Activation)     (None, 55, 37, 32)   0           ['batch_normalization_71[1][0]'] 
                                                                                                  
 conv2d_72 (Conv2D)             (None, 55, 37, 32)   9216        ['activation_69[1][0]']          
                                                                                                  
 batch_normalization_72 (BatchN  (None, 55, 37, 32)  128         ['conv2d_72[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_33 (TFOpL  (None, 55, 37, 32)  0           ['batch_normalization_72[1][0]', 
 ambda)                                                           'activation_68[1][0]']          
                                                                                                  
 activation_70 (Activation)     (None, 55, 37, 32)   0           ['tf.__operators__.add_33[1][0]']
                                                                                                  
 conv2d_73 (Conv2D)             (None, 55, 37, 32)   9216        ['activation_70[1][0]']          
                                                                                                  
 batch_normalization_73 (BatchN  (None, 55, 37, 32)  128         ['conv2d_73[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_71 (Activation)     (None, 55, 37, 32)   0           ['batch_normalization_73[1][0]'] 
                                                                                                  
 conv2d_74 (Conv2D)             (None, 55, 37, 32)   9216        ['activation_71[1][0]']          
                                                                                                  
 batch_normalization_74 (BatchN  (None, 55, 37, 32)  128         ['conv2d_74[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_34 (TFOpL  (None, 55, 37, 32)  0           ['batch_normalization_74[1][0]', 
 ambda)                                                           'activation_70[1][0]']          
                                                                                                  
 activation_72 (Activation)     (None, 55, 37, 32)   0           ['tf.__operators__.add_34[1][0]']
                                                                                                  
 conv2d_75 (Conv2D)             (None, 28, 19, 64)   18432       ['activation_72[1][0]']          
                                                                                                  
 batch_normalization_75 (BatchN  (None, 28, 19, 64)  256         ['conv2d_75[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_73 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_75[1][0]'] 
                                                                                                  
 conv2d_76 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_73[1][0]']          
                                                                                                  
 conv2d_77 (Conv2D)             (None, 28, 19, 64)   2048        ['activation_72[1][0]']          
                                                                                                  
 batch_normalization_76 (BatchN  (None, 28, 19, 64)  256         ['conv2d_76[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 batch_normalization_77 (BatchN  (None, 28, 19, 64)  256         ['conv2d_77[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_35 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_76[1][0]', 
 ambda)                                                           'batch_normalization_77[1][0]'] 
                                                                                                  
 activation_74 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_35[1][0]']
                                                                                                  
 conv2d_78 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_74[1][0]']          
                                                                                                  
 batch_normalization_78 (BatchN  (None, 28, 19, 64)  256         ['conv2d_78[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_75 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_78[1][0]'] 
                                                                                                  
 conv2d_79 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_75[1][0]']          
                                                                                                  
 batch_normalization_79 (BatchN  (None, 28, 19, 64)  256         ['conv2d_79[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_36 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_79[1][0]', 
 ambda)                                                           'activation_74[1][0]']          
                                                                                                  
 activation_76 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_36[1][0]']
                                                                                                  
 conv2d_80 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_76[1][0]']          
                                                                                                  
 batch_normalization_80 (BatchN  (None, 28, 19, 64)  256         ['conv2d_80[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_77 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_80[1][0]'] 
                                                                                                  
 conv2d_81 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_77[1][0]']          
                                                                                                  
 batch_normalization_81 (BatchN  (None, 28, 19, 64)  256         ['conv2d_81[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_37 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_81[1][0]', 
 ambda)                                                           'activation_76[1][0]']          
                                                                                                  
 activation_78 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_37[1][0]']
                                                                                                  
 conv2d_82 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_78[1][0]']          
                                                                                                  
 batch_normalization_82 (BatchN  (None, 28, 19, 64)  256         ['conv2d_82[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_79 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_82[1][0]'] 
                                                                                                  
 conv2d_83 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_79[1][0]']          
                                                                                                  
 batch_normalization_83 (BatchN  (None, 28, 19, 64)  256         ['conv2d_83[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_38 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_83[1][0]', 
 ambda)                                                           'activation_78[1][0]']          
                                                                                                  
 activation_80 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_38[1][0]']
                                                                                                  
 conv2d_84 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_80[1][0]']          
                                                                                                  
 batch_normalization_84 (BatchN  (None, 28, 19, 64)  256         ['conv2d_84[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_81 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_84[1][0]'] 
                                                                                                  
 conv2d_85 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_81[1][0]']          
                                                                                                  
 batch_normalization_85 (BatchN  (None, 28, 19, 64)  256         ['conv2d_85[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_39 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_85[1][0]', 
 ambda)                                                           'activation_80[1][0]']          
                                                                                                  
 activation_82 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_39[1][0]']
                                                                                                  
 conv2d_86 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_82[1][0]']          
                                                                                                  
 batch_normalization_86 (BatchN  (None, 28, 19, 64)  256         ['conv2d_86[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_83 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_86[1][0]'] 
                                                                                                  
 conv2d_87 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_83[1][0]']          
                                                                                                  
 batch_normalization_87 (BatchN  (None, 28, 19, 64)  256         ['conv2d_87[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_40 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_87[1][0]', 
 ambda)                                                           'activation_82[1][0]']          
                                                                                                  
 activation_84 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_40[1][0]']
                                                                                                  
 conv2d_88 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_84[1][0]']          
                                                                                                  
 batch_normalization_88 (BatchN  (None, 28, 19, 64)  256         ['conv2d_88[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_85 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_88[1][0]'] 
                                                                                                  
 conv2d_89 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_85[1][0]']          
                                                                                                  
 batch_normalization_89 (BatchN  (None, 28, 19, 64)  256         ['conv2d_89[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_41 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_89[1][0]', 
 ambda)                                                           'activation_84[1][0]']          
                                                                                                  
 activation_86 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_41[1][0]']
                                                                                                  
 conv2d_90 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_86[1][0]']          
                                                                                                  
 batch_normalization_90 (BatchN  (None, 28, 19, 64)  256         ['conv2d_90[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_87 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_90[1][0]'] 
                                                                                                  
 conv2d_91 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_87[1][0]']          
                                                                                                  
 batch_normalization_91 (BatchN  (None, 28, 19, 64)  256         ['conv2d_91[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_42 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_91[1][0]', 
 ambda)                                                           'activation_86[1][0]']          
                                                                                                  
 activation_88 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_42[1][0]']
                                                                                                  
 conv2d_92 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_88[1][0]']          
                                                                                                  
 batch_normalization_92 (BatchN  (None, 28, 19, 64)  256         ['conv2d_92[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_89 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_92[1][0]'] 
                                                                                                  
 conv2d_93 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_89[1][0]']          
                                                                                                  
 batch_normalization_93 (BatchN  (None, 28, 19, 64)  256         ['conv2d_93[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_43 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_93[1][0]', 
 ambda)                                                           'activation_88[1][0]']          
                                                                                                  
 activation_90 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_43[1][0]']
                                                                                                  
 conv2d_94 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_90[1][0]']          
                                                                                                  
 batch_normalization_94 (BatchN  (None, 28, 19, 64)  256         ['conv2d_94[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_91 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_94[1][0]'] 
                                                                                                  
 conv2d_95 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_91[1][0]']          
                                                                                                  
 batch_normalization_95 (BatchN  (None, 28, 19, 64)  256         ['conv2d_95[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_44 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_95[1][0]', 
 ambda)                                                           'activation_90[1][0]']          
                                                                                                  
 activation_92 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_44[1][0]']
                                                                                                  
 conv2d_96 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_92[1][0]']          
                                                                                                  
 batch_normalization_96 (BatchN  (None, 28, 19, 64)  256         ['conv2d_96[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_93 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_96[1][0]'] 
                                                                                                  
 conv2d_97 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_93[1][0]']          
                                                                                                  
 batch_normalization_97 (BatchN  (None, 28, 19, 64)  256         ['conv2d_97[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_45 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_97[1][0]', 
 ambda)                                                           'activation_92[1][0]']          
                                                                                                  
 activation_94 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_45[1][0]']
                                                                                                  
 conv2d_98 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_94[1][0]']          
                                                                                                  
 batch_normalization_98 (BatchN  (None, 28, 19, 64)  256         ['conv2d_98[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 activation_95 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_98[1][0]'] 
                                                                                                  
 conv2d_99 (Conv2D)             (None, 28, 19, 64)   36864       ['activation_95[1][0]']          
                                                                                                  
 batch_normalization_99 (BatchN  (None, 28, 19, 64)  256         ['conv2d_99[1][0]']              
 ormalization)                                                                                    
                                                                                                  
 tf.__operators__.add_46 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_99[1][0]', 
 ambda)                                                           'activation_94[1][0]']          
                                                                                                  
 activation_96 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_46[1][0]']
                                                                                                  
 conv2d_100 (Conv2D)            (None, 28, 19, 64)   36864       ['activation_96[1][0]']          
                                                                                                  
 batch_normalization_100 (Batch  (None, 28, 19, 64)  256         ['conv2d_100[1][0]']             
 Normalization)                                                                                   
                                                                                                  
 activation_97 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_100[1][0]']
                                                                                                  
 conv2d_101 (Conv2D)            (None, 28, 19, 64)   36864       ['activation_97[1][0]']          
                                                                                                  
 batch_normalization_101 (Batch  (None, 28, 19, 64)  256         ['conv2d_101[1][0]']             
 Normalization)                                                                                   
                                                                                                  
 tf.__operators__.add_47 (TFOpL  (None, 28, 19, 64)  0           ['batch_normalization_101[1][0]',
 ambda)                                                           'activation_96[1][0]']          
                                                                                                  
 activation_98 (Activation)     (None, 28, 19, 64)   0           ['tf.__operators__.add_47[1][0]']
                                                                                                  
 batch_normalization_102 (Batch  (None, 28, 19, 64)  256         ['activation_98[1][0]']          
 Normalization)                                                                                   
                                                                                                  
 activation_99 (Activation)     (None, 28, 19, 64)   0           ['batch_normalization_102[1][0]']
                                                                                                  
 flatten (Flatten)              (None, 34048)        0           ['activation_99[1][0]']          
                                                                                                  
 dense (Dense)                  (None, 1)            34049       ['flatten[1][0]']                
                                                                                                  
==================================================================================================
Total params: 3,159,617
Trainable params: 3,147,777
Non-trainable params: 11,840
__________________________________________________________________________________________________
/home/linhlh12/comma-calib-challenge/model_resnet.py:157: UserWarning: `Model.fit_generator` is deprecated and will be removed in a future version. Please use `Model.fit`, which supports generators.
  model.fit_generator(batch_generator_2inputs(data_dir_train, x_train, y_train, batch_size, True),
Epoch 1/15
2021-12-18 20:27:15.913563: I tensorflow/stream_executor/cuda/cuda_dnn.cc:366] Loaded cuDNN version 8301
2021-12-18 20:27:16.266180: I tensorflow/core/platform/default/subprocess.cc:304] Start cannot spawn child process: No such file or directory
2021-12-18 20:27:17.651531: W tensorflow/core/common_runtime/bfc_allocator.cc:275] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.50GiB with freed_by_count=0. The caller indicates that this is not a failure, but may mean that there could be performance gains if more memory were available.
2021-12-18 20:27:17.651589: W tensorflow/core/common_runtime/bfc_allocator.cc:275] Allocator (GPU_0_bfc) ran out of memory trying to allocate 2.50GiB with freed_by_count=0. The caller indicates that this is not a failure, but may mean that there could be performance gains if more memory were available.
250/250 [==============================] - 583s 2s/step - loss: 1.7489 - val_loss: 13.7843
Epoch 2/15
250/250 [==============================] - 574s 2s/step - loss: 0.0288 - val_loss: 3.2047
Epoch 3/15
250/250 [==============================] - 576s 2s/step - loss: 0.0218 - val_loss: 1.2943
Epoch 4/15
250/250 [==============================] - 576s 2s/step - loss: 0.0080 - val_loss: 1.4715
Epoch 5/15
250/250 [==============================] - 576s 2s/step - loss: 0.0551 - val_loss: 0.2824
Epoch 6/15
250/250 [==============================] - 577s 2s/step - loss: 0.0316 - val_loss: 0.0878
Epoch 7/15
250/250 [==============================] - 575s 2s/step - loss: 0.0048 - val_loss: 0.0880
Epoch 8/15
250/250 [==============================] - 574s 2s/step - loss: 0.0434 - val_loss: 0.0569
Epoch 9/15
250/250 [==============================] - 575s 2s/step - loss: 0.0260 - val_loss: 0.0659
Epoch 10/15
250/250 [==============================] - 575s 2s/step - loss: 0.0094 - val_loss: 0.0602
Epoch 11/15
250/250 [==============================] - 576s 2s/step - loss: 0.0272 - val_loss: 0.0322
Epoch 12/15
250/250 [==============================] - 576s 2s/step - loss: 0.0118 - val_loss: 0.0278
Epoch 13/15
250/250 [==============================] - 576s 2s/step - loss: 0.0171 - val_loss: 0.0286
Epoch 14/15
250/250 [==============================] - 576s 2s/step - loss: 0.0283 - val_loss: 0.0415
Epoch 15/15
250/250 [==============================] - 575s 2s/step - loss: 0.0061 - val_loss: 0.0129
Epoch 1/15
250/250 [==============================] - 584s 2s/step - loss: 0.6670 - val_loss: 9.1117
Epoch 2/15
250/250 [==============================] - 575s 2s/step - loss: 0.0043 - val_loss: 5.8622
Epoch 3/15
250/250 [==============================] - 577s 2s/step - loss: 0.0071 - val_loss: 5.0444
Epoch 4/15
250/250 [==============================] - 574s 2s/step - loss: 0.0166 - val_loss: 6.5778
Epoch 5/15
250/250 [==============================] - 576s 2s/step - loss: 0.0209 - val_loss: 7.8486
Epoch 6/15
250/250 [==============================] - 574s 2s/step - loss: 0.0238 - val_loss: 7.0515
Epoch 7/15
250/250 [==============================] - 574s 2s/step - loss: 0.0243 - val_loss: 7.4567
Epoch 8/15
250/250 [==============================] - 578s 2s/step - loss: 0.0165 - val_loss: 1.4507
Epoch 9/15
250/250 [==============================] - 574s 2s/step - loss: 0.0313 - val_loss: 3.3364
Epoch 10/15
250/250 [==============================] - 576s 2s/step - loss: 0.0120 - val_loss: 0.3346
Epoch 11/15
250/250 [==============================] - 577s 2s/step - loss: 0.0251 - val_loss: 0.0253
Epoch 12/15
250/250 [==============================] - 577s 2s/step - loss: 0.0122 - val_loss: 7.5907e-04
Epoch 13/15
250/250 [==============================] - 577s 2s/step - loss: 0.0158 - val_loss: 0.0055
Epoch 14/15
250/250 [==============================] - 574s 2s/step - loss: 0.0337 - val_loss: 0.0069
Epoch 15/15
250/250 [==============================] - 574s 2s/step - loss: 0.0050 - val_loss: 0.0375
Epoch 1/15
250/250 [==============================] - 583s 2s/step - loss: 0.6882 - val_loss: 26.1572
Epoch 2/15
250/250 [==============================] - 576s 2s/step - loss: 0.0599 - val_loss: 60.7670
Epoch 3/15
250/250 [==============================] - 575s 2s/step - loss: 0.0268 - val_loss: 24.0139
Epoch 4/15
250/250 [==============================] - 575s 2s/step - loss: 0.0672 - val_loss: 111.5180
Epoch 5/15
250/250 [==============================] - 576s 2s/step - loss: 0.1179 - val_loss: 56.7534
Epoch 6/15
250/250 [==============================] - 573s 2s/step - loss: 0.0132 - val_loss: 106.5163
Epoch 7/15
250/250 [==============================] - 574s 2s/step - loss: 0.0041 - val_loss: 148.5795
Epoch 8/15
250/250 [==============================] - 573s 2s/step - loss: 0.0030 - val_loss: 92.1488
Epoch 9/15
250/250 [==============================] - 574s 2s/step - loss: 0.0197 - val_loss: 145.0285
Epoch 10/15
250/250 [==============================] - 574s 2s/step - loss: 0.0304 - val_loss: 86.9877
Epoch 11/15
250/250 [==============================] - 577s 2s/step - loss: 0.0027 - val_loss: 81.2768
Epoch 12/15
250/250 [==============================] - 575s 2s/step - loss: 22.6053 - val_loss: 71566232.0000
Epoch 13/15
250/250 [==============================] - 573s 2s/step - loss: 1.7842 - val_loss: 297.3990
Epoch 14/15
250/250 [==============================] - 574s 2s/step - loss: 0.0546 - val_loss: 211.5971
Epoch 15/15
250/250 [==============================] - 576s 2s/step - loss: 0.0351 - val_loss: 203.9547
Epoch 1/15
250/250 [==============================] - 583s 2s/step - loss: 0.6864 - val_loss: 3351.3677
Epoch 2/15
250/250 [==============================] - 579s 2s/step - loss: 0.0380 - val_loss: 2046.0480
Epoch 3/15
250/250 [==============================] - 576s 2s/step - loss: 0.0450 - val_loss: 2156.5088
Epoch 4/15
250/250 [==============================] - 575s 2s/step - loss: 0.0635 - val_loss: 2590.4248
Epoch 5/15
250/250 [==============================] - 577s 2s/step - loss: 0.0727 - val_loss: 1374.1630
Epoch 6/15
250/250 [==============================] - 576s 2s/step - loss: 0.0195 - val_loss: 1050.3917
Epoch 7/15
250/250 [==============================] - 577s 2s/step - loss: 0.0612 - val_loss: 1007.1472
Epoch 8/15
250/250 [==============================] - 575s 2s/step - loss: 0.0466 - val_loss: 424.7447
Epoch 9/15
250/250 [==============================] - 576s 2s/step - loss: 0.0245 - val_loss: 433.5902
Epoch 10/15
250/250 [==============================] - 576s 2s/step - loss: 0.1785 - val_loss: 1713.5555
Epoch 11/15
250/250 [==============================] - 577s 2s/step - loss: 0.0480 - val_loss: 364.2838
Epoch 12/15
250/250 [==============================] - 576s 2s/step - loss: 0.0091 - val_loss: 333.9545
Epoch 13/15
250/250 [==============================] - 577s 2s/step - loss: 0.0053 - val_loss: 421.7980
Epoch 14/15
250/250 [==============================] - 577s 2s/step - loss: 0.0060 - val_loss: 317.3746
Epoch 15/15
250/250 [==============================] - 576s 2s/step - loss: 0.0059 - val_loss: 272.3720