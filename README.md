# image_recognition

This is an image recognition machine learning app that does image prediction using pre-existing models and the Image AI library.

Click here to run the code in your browser:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kdhenderson/image_recognition/master)
  - Click on the 'New' dropdown button and select 'Terminal'
  - Run the program from the command line like this:
	$ python3 brain.py

This is what the program does step-by-step:
  - Assigns the execution path to get images from the current working directory (cwd) via the OS library.
  - Instantiates an image prediction object from the ImagePrediction class imported from Image AI library's prediction module.
  - Sets the model type. (Image AI can use 1 of 4 pre-built models for image prediction.) I chose to use SqueezeNet and trade off a bit of accuracy for a smaller sized model.
  - Sets the model path. (In this case, I downloaded the SqueezeNet model to my cwd).
  - Loads the model.
  - Gives it the image and the number of predictions to make. 
  - Outputs each prediction and the confidence of the model for that prediction.

This program is written to process one image or multiple images. For multiple images (code is commented out), this is what the code does:
  - Loops to find all jpg or png files in the cwd and adds them to an array.
  - Gives that array to the predictMultipleImages function to run the model.
  - Creates a results array with each image, a defined number of predictions for each and the probability of those.
  - Outputs the results for each image to the console.


Dependencies:
  - Image AI has some dependencies listed in the requirements.txt file.
		- Machine learning libraries: Tensorflow and Keras
		- Image processing library: OpenCV
  - You will need to download the SqueezeNet model (in the repository). 
  - The repo also contains some sample images. 
  - Install the requirements using pip install -r requirements.txt.
  - Make sure you use Python 3.
  - You may want to use a virtual environment for this.
  - Download the model and images to the same directory as the py file.


Usage:
  - Run the program from the command line.
