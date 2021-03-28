import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import mtcnn as mn
import numpy as np
import matplotlib.pyplot as plt
import cv2 
import zipfile

class FaceDetector:
    def __init__(self, image_height = 200, image_width = 200):
        self.target_height = image_height
        self.target_width = image_width
        self.faceDetector = mn.MTCNN()
        self.valid_images = [".jpg"]

    def detect_face(self, path_to_image):
        if self.__is_valid(path_to_image):
            image_as_numpy = self.__convert_image_to_numpy_array(path_to_image)
            face_coordinates = self.faceDetector.detect_faces(image_as_numpy)
            if len(face_coordinates) == 1:
                result = self.__cut_face_area(image_as_numpy, face_coordinates)
                print('Face successfully detected.')
                return result
            print('Face not found.')
            return None
        else:
            print('Invalid file format.')
            return None

    def __cut_face_area(self, image_as_numpy, face_coordinates):
        x1, y1, width, height = face_coordinates[0]['box']
        x1, y1 = abs(x1), abs(y1)
        x2 = x1 + width
        y2 = y1 + height
        return image_as_numpy[y1:y2, x1:x2]
            
    def __convert_image_to_numpy_array(self, path):
        image = cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pixels = np.asarray(image)
        return pixels

    def __is_valid(self, path):
        filename, file_extension = os.path.splitext(path)
        if file_extension.lower() not in self.valid_images:
            return False
        return True
