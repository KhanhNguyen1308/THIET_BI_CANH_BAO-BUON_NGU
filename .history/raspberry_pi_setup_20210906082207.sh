#!/bin/bash
sudo apt-get -y install ffmpeg python3-opencv
sudo apt-get -y install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
sudo pip3 install mediapipe-rpi4
wget https://github.com/Qengineering/Install-OpenCV-Raspberry-Pi-32-bits/raw/main/OpenCV-4-5-2.sh
sudo chmod 755 ./OpenCV-4-5-2.sh
./OpenCV-4-5-2.sh