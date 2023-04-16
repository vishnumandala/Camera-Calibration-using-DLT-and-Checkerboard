# PROJECT 3
## ENPM673 - Perception for Autonomous Robots

## Dependencies
1. python 3.11 (any version above 3 should work)
2. Python running IDE (I used VS Code)

## Libraries
1. OpenCV
2. NumPy
3. Matplotlib
4. Glob

## Contents
1. problem1.py
2. problem2.py
3. checkerboardPattern.pdf
4. Calibration_Imgs
    - IMG_20170209_042606.jpg
    - IMG_20170209_042608.jpg
    - IMG_20170209_042610.jpg
    - IMG_20170209_042612.jpg
    - IMG_20170209_042614.jpg
    - IMG_20170209_042616.jpg
    - IMG_20170209_042619.jpg
    - IMG_20170209_042621.jpg
    - IMG_20170209_042624.jpg
    - IMG_20170209_042627.jpg
    - IMG_20170209_042629.jpg
    - IMG_20170209_042630.jpg
    - IMG_20170209_042634.jpg
5. vishnum_proj3.pdf
6. README.md
7. problem2_output.png

## Installation Instructions
1. Download the zip file and extract it
2. Install python and the required dependencies: pip install opencv-python numpy matplotlib glob

## Problem 1 - Camera Calibration with Direct Linear Transformation (DLT) algorithm and Gram-Schmidt RQ Decomposition
This Python script is an implementation of the Direct Linear Transformation (DLT) algorithm for camera calibration. The algorithm takes in a set of 3D world points and their corresponding 2D image points, and returns the projection matrix, intrinsic matrix, rotation matrix, and translation vector of the camera by using Gram-Schmidt decomposition. It also computes the reprojection error for each point to evaluate the accuracy of the calibration.

### Features
1. Computes the Projection Matrix using Direct Linear Transformation
2. Computes Intrinsic Matrix (K), Rotation Matrix (R) and Translation Vector (t) by decomposing P matrix using Gram-Schmidt RQ decomposition
3. Calculates the reprojection error for each point

### Usage
1. Define the image points and world points in the script.
2. Run the code: problem1.py

### Example Output

Projection Matrix (P):  
[[ 0.036223 -0.002215 -0.088324  0.954089]  
[-0.025383  0.083056 -0.028002  0.268827]  
[-0.000035 -0.000003 -0.00004   0.001261]]   

Intrinsic Matrix (K):  
[[1619.01802    -1.89271   800.113193]  
[   0.       1612.025941  616.150419]  
[   0.         -0.          1.      ]]   

Rotation Matrix (R):  
[[ 0.749486  0.00587  -0.661994]  
[-0.045356  0.998066 -0.0425  ]  
[-0.660464 -0.061879 -0.748303]]   

Translation Vector (t):  
[[-0.000034]  
[-0.000315]  
[ 0.001261]] 

Reprojection Error for Point 1 is: 0.28561276727805496
Reprojection Error for Point 2 is: 0.9725828452229532
Reprojection Error for Point 3 is: 1.036081784374865
Reprojection Error for Point 4 is: 0.45408628677326207
Reprojection Error for Point 5 is: 0.19089831889735914
Reprojection Error for Point 6 is: 0.3189920832714891
Reprojection Error for Point 7 is: 0.19594240534327106
Reprojection Error for Point 8 is: 0.30829602844222703

## Problem 2 - Camera Calibration using OpenCV and Checkerboard
This code performs chessboard calibration on a set of images using OpenCV. The calibration process finds the intrinsic matrix K which can then be used to find the parameters of the camera, such as focal length and principal point, and the distortion coefficients. It also computes the Reprojection Error for each image.

### Features
1. Computes the intrinsic matrix of a camera
2. Uses checkboard functions to identify, draw and project corners
3. Computes reprojection error for each image

### Usage
1. Place the images to be calibrated in a folder named Calibration_Imgs in the same directory as the code.
2. Update the square_size and pattern_size variables in lines 6-7 to match the dimensions of the calibration target used.
3. Run the code: problem2.py

## Output
![Images with corners drawn and reprojection errors](https://github.com/vishnumandala/Camera-Calibration-using-DLT-and-Checkerboard/blob/main/problem2_output.png)
