import numpy as np
import os
import cv2 

from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, Activation
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, LearningRateScheduler
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import VGG16

class ConvolutionalNeuralNetwork:
    
    def __init__(self, width = 200, height = 200, batchSize = 16, epochs = 25, classes = 2, vgg16_path = ''):
        self.width, self.height = width, height
        self.batch_size = batchSize
        self.epochs = epochs
        self.classes = classes
        self.input_shape = (self.width, self.height, 3)
        self.vgg16_path = vgg16_path

        self.train_generator = ImageDataGenerator(
            rescale=1. / 255,
            rotation_range=10, 
            zoom_range = 0.1,  
            width_shift_range=0.1,  
            height_shift_range=0.1,  
            vertical_flip=False,
            horizontal_flip=True
        )

        self.test_generator = ImageDataGenerator(rescale=1. / 255)
        
        self.train_flow = None
        self.test_flow = None

        self.train_samples = 1114
        self.test_samples = 99
        return

    def __load_data(self, train_path, test_path):
        self.train_flow = self.train_generator.flow_from_directory(
            train_path,
            target_size=(self.width, self.height),
            batch_size=self.batch_size,
            class_mode='categorical')

        self.test_flow = self.test_generator.flow_from_directory(
            test_path,
            target_size=(self.width, self.height),
            batch_size=self.batch_size,
            class_mode='categorical')
    
    def fit_data(self, train_path, test_path):
        self.__load_data(train_path, test_path)
        model = self.__make_model('sigmoid')
        optimizer = RMSprop(lr=1e-5, decay=1e-7)
        model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])
        history = model.fit_generator(
            self.train_flow,
            steps_per_epoch=self.train_samples // self.batch_size,
            epochs=self.epochs,
            validation_data=self.test_flow,
            validation_steps=self.test_samples // self.batch_size)

    def __make_model(self, activation_function='sigmoid'):
        base_model = None
        base_model = VGG16(weights=None, include_top=False, input_shape=self.input_shape)
        base_model.load_weights(self.vgg16_path)
        
        top_model = Sequential()
        top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
        for i in range(2):
            top_model.add(Dense(4096, activation='relu'))
            top_model.add(Dropout(0.5))
        top_model.add(Dense(self.classes, activation=activation_function))

        model = None
        model = Model(inputs=base_model.input, outputs=top_model(base_model.output))
        return model

    