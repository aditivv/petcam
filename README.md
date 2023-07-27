## Petcam

This model is used to detect whether there is a person or a pet in front of the camera, which can help when detecting intruders at home as opposed to pets running around the house.

## The Algorithm
The algorithim is used by recording a video on a Logitech webcam - supported by Jetson nano. It uses a 2GB Jetson Nano, and so it uses it a preflashed SD card flashed from the NVIDIA webpage. It uses imagenet to classify what is in front of the camera, and whether it is an animal or an intruder/person.

## Running this project
1. Connect to your Jetson Nano via VSCODE. 
2. Connect your Webcam (preferably logitech)
3. Ensure that you have the proper things installed. The Renet18.onnx and all others like that - the ones that say resnet18.onnx and the final_project2.py. Also, esure that you have the labels.txt file.
4. Since using teh preflashed SD card, there sould be a docker container. This is accesable by implementing this code. Change directories into jetson-inference/build/aarch64/bin. - use this code if your in the home.$ cd jetson-inference/build/aarch64/bin
5. Then run this code -$ ./docker/run.sh --volume /home/(username)/final-projects:/final-projects - the code moves the final-projects folder into the docker container so that the line from PIL import Image runs without an error.
6a. The run the following code - $ python3 petcam.py --network=facenet (webcam name here)
6b. You should see a video popup of your face. Note how it is not a smooth stream of images. It should be a headshot of you and your face, and there should be some blakc space.
7. The model is up and running, and so you should just put your face in clear view infront of the camera and watch as it tries to predict your age!

