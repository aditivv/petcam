#!/usr/bin/python3

# importing needed stuff
import jetson.inference
import jetson.utils

# setting up camera and allowing video to save
net = jetson.inference.detectNet("ssd-mobilenet-v2",threshold=0.5)
camera = jetson.utils.videoSource("/dev/video0")
display = jetson.utils.videoOutput("file://where_is_my_pet.mp4")

# live camera
while True:
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS())) 

	# get ClassID for every detected object
	for detection in detections:
		class_idx = detection.ClassID 
		class_desc = net.GetClassDesc(class_idx)
		print(class_desc)

		# if ClassID is a cat or a dog, notify user
		if class_desc == str("cat") or str("dog"):
			print("Your pet is visible in front of the camera!")
