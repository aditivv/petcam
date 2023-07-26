#!/usr/bin/python3

# importing needed stuff
from jetson_inference import imageNet
from jetson_utils import videoSource, videoOutput

# setting up detectnet and camera as video source
net = imageNet("ssd-mobilenet-v2",threshold=0.5)
camera = videoSource("/dev/video0")
display = videoOutput("file://my_petcam.mp4")

# live camera
while display.IsStreaming():
	
