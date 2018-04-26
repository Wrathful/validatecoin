import cv2
import numpy as np
import os,shutil, random
from keras import backend as K
from keras.models import load_model


class ClassModel:
    def __init__(self):         # data
        self.model = load_model('model.hdf5')

    def predict(self,img):
        return self.model.predict(img.reshape(1,256,256,3))
