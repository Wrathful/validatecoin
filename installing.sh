#!/bin/bash
sudo apt install python3.6
sudo apt install python3-pip
sudo -H pip3 install keras
sudo apt-get install python3-opencv
sudo -H pip3 install flask
sudo -H pip3 install theano
sed -i 's/thensorflow/theano/' ~/.keras/keras.json
sudo -H pip3 install numpy
sudo -H pip3 install h5py
sudo -H pip3 install pandas
