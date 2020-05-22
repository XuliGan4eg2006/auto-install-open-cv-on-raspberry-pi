import os

os.system("sudo apt-get dist-upgrade")
os.system("pip3 install tensorflow")
os.system("sudo apt-get install libatlas-base-dev")
os.system("sudo pip3 install pillow lxml jupyter matplotlib cython")
os.system("sudo apt-get install python-tk")
os.system("sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-de")
os.system("sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev")
os.system("sudo apt-get install libxvidcore-dev libx264-dev")
os.system("sudo apt-get install qt4-dev-tools libatlas-base-dev")
os.system("sudo pip3 install opencv-python")
os.system("sudo apt-get install protobuf-compiler")
os.system("mkdir tensorflow1")
os.system("cd tensorflow1")
os.system("git clone --depth 1 https://github.com/tensorflow/models.git")
with open(os.path.expanduser("~/.bashrc"), "a") as f:
	f.write("\n\nexport PYTHONPATH=$PYTHONPATH:/home/pi/tensorflow1/models/research:/home/pi/tensorflow1/models/research/slim")
os.system("cd /home/pi/tensorflow1/models/research")
os.system("protoc object_detection/protos/*.proto --python_out=.")
os.system("cd /home/pi/tensorflow1/models/research/object_detection")
os.system("wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz")
os.system("tar -xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz")
os.system("wget https://raw.githubusercontent.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi/master/Object_detection_picamera.py")
print("Всё прошло успешно! Теперь вы можете распозеовать обекты! ")
