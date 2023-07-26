#!/usr/bin/python3

# importing needed stuff
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

# setting up detectnet and camera as video source
net = jetson.inference.detectNet("ssd-mobilenet-v2",threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("file://my_petcam.mp4")

# live camera
while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS())) 

	# get ClassID for every detected object
	for detection in detections:
		class_id = detection.ClassID 
		class_name = net.GetClassDesc(class_id)
		print(class_name)

		# if ClassID is a cat or a dog, notify user
		if class_name == str("cat") or str("dog"):
			print("Your pet is visible in front of the camera!")
