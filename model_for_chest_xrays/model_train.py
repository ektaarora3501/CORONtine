
'''Copyright notice..
The work, code and algorithm belongs to team Dev.ino .The team must be acknowledged for use of any portion of the project/code . The team Dev.ino reserves all rights on the code and the dataset .
We would be happy to mention https://github.com/ieee8023/covid-chestxray-dataset for their dataset for Chest X-Ray model creation

Team Dev.ino
Developers
Krishna Ojha
Ekta Arora
'''



import matplotlib.pyplot as plt
import numpy as np
import pandas as pdb
from keras.models import Sequential
from keras.layers import Dropout,Dense,Conv2D,Flatten,MaxPooling2D,Activation,BatchNormalization
import os
from keras.optimizers import Adam
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator,load_img



WIDTH=200
HEIGHT=200
IMAGE_SIZE=(200,200,3)
SAMPLES=64*2
BATCH_SIZE=6
EPOCHS = 15

train_dir = "/home/ekta3501/opensource/Dev.ino_HackCovid19/chest/train"

model = Sequential()

model.add(Conv2D(32,(3,3),input_shape=(IMAGE_SIZE)))
model.add(Activation('relu'))
# model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Dropout(0.25))

model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
# model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
# model.add(Dropout(0.25))

model.add(Conv2D(128,(3,3),activation='relu'))
# model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(128,activation='relu'))
# model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Dense(2))
model.add(Activation('sigmoid'))


# TODO: check for loss = mean_squared_error and optimizer Adam
# Currently model is optimized with the added loss function , #TEST: on live video

model.compile(loss='categorical_crossentropy',optimizer=Adam(),metrics=['accuracy'],)

model.summary()

train_data_gen = ImageDataGenerator(

           rescale = 1./255,
           shear_range=0.2,
           zoom_range=0.2,
           horizontal_flip=True,
        )

training_generator = train_data_gen.flow_from_directory(
         train_dir,
         target_size = (WIDTH,HEIGHT),
         batch_size=BATCH_SIZE,
         class_mode = "categorical",
)

print(training_generator.class_indices)

model.fit_generator( training_generator,
      epochs = EPOCHS,
      steps_per_epoch = SAMPLES//BATCH_SIZE,
      verbose = 1,
)

#TODO: assure model is not overfitting

#batch size , epochs
model.save('model1_6_15.h5')
