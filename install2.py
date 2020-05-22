import os

os.system("cd /home/pi/tensorflow1/models/research")
os.system("protoc object_detection/protos/*.proto --python_out=.")
os.system("cd /home/pi/tensorflow1/models/research/object_detection")
os.system("wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz")
os.system("tar -xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz")
os.system("wget https://raw.githubusercontent.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi/master/Object_detection_picamera.py")
print("Всё прошло успешно! Теперь вы можете распозеовать обекты! ")
