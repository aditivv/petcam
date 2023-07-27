## PetorNot

This model is used to detect whether security footage from house cameras actually caught any intruders or simply pets running around the house. It does this using the Imagenet classification network to classify whether there is a human (intruder) or pet (cat or dog) in front of the camera. This can be very helpful by allowing users to run through long security footage and detect intruders using the model rather than watching the entire video and possibly skipping through important points in time or zoning out and missing important details.

## The Algorithm
The algorithim is used by reading image or video data and classifying whether it contains a dog, cat, or human (intruder)

## What you need
1. Jetson Nano
2. VScode (To view output; you will need to connect to your Nano via VScode)

## Running this project
1. Download resnet18.onnx and labels.txt onto your Jetson Nano from this project
2. Clone the jetson-inference project from GitHub using "git clone --recursive [https://github.com/dusty-nv/jetson-inference](url)" and change directories into it
3. Make sure to have python packages installed using "sudo apt-get install libpython3-dev python3-numpy"
4. Go to jetson-inference/python/training/classification/models and create a new directory for this model using "mkdir petornot". Do the same in jetson-inference/python/training/classification/data.
5. Copy the downloaded model and text file from (1.) onto jetson-inference/python/training/classification/models/petornot
6. Add any data that you would like to test the model on (For example, security footage) in jetson-inference/python/training/classification/data/petornot
7. Go back to jetson-inference/python/training/classification
8. Set the NET and DATASET models using "NET=models/petornot" and "DATASET=data/petornot"
9. Run the model using "imagenet.py --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt $DATASET/(YOUR DATA FILE) (WHAT YOU WOULD LIKE TO SAVE OUTPUT AS)"
10. SSN into the jetson-inference folder in VScode to view the new saved file of your classified data (should be under python/training/classification)!

Watch this video for a tutorial on how to complete steps 7-10: [https://youtu.be/LbBmhrWvsyc]

