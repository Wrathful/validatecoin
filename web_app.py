import cv2
import numpy as np
import os,shutil, random

from keras.models import load_model


model = load_model('model_moneti.hdf5')
#cap = cv2.VideoCapture(0)
#for i in range(30):
#   cap.read()
#i=0
while True:
   print("Чтобы сделать снимок с веб-камеры нажмите enter")
   name = input()
   cap = cv2.VideoCapture(0)
   ret, frame = cap.read()
   cv2.imwrite('cam.png', frame)
   img = cv2.imread('cam.png')
   resized_image = cv2.resize(img, (256, 256))
   print(model.predict(resized_image.reshape(1,256,256,3)))
   #i=i+1
   cap.release()


