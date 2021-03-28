from tensorflow import keras
import os
import numpy as np
import cv2
from keras.preprocessing import image
import matplotlib.pyplot as plt

class Tester:
    def __init__(self, test_path, model_path):
        self.labels = ['Keira Knightley', 'Natalie Portman']
        self.test_path = test_path
        self.model = keras.models.load_model(model_path)

    def __showResult(self, result, index, img):
        plt.figure()
        plt.axis('off')
        plt.title("{}, {:.2f}%".format(self.labels[index], result[index]*100))
        plt.imshow(img)
        plt.show()

    def run_test(self, image_width, image_height):
        for file in os.listdir(self.test_path):
            imagePath = self.test_path + "/" + str(file)
            img = image.load_img(imagePath, target_size=(image_width, image_height))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x /= 255.

            result = self.model.predict(x)
            result = np.squeeze(result)
            resultIndex = np.argmax(result)
            self.__showResult(result, resultIndex, img)