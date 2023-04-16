import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

square_size = 21.5  # Size of each square in millimeters
pattern_size = (9, 6)   # Number of inner corners along the X and Y axis

obj = np.zeros((pattern_size[0]*pattern_size[1], 3), np.float32)   # Prepare object points for the calibration target 
obj[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)   # Create a grid of points
obj *= square_size    # Scale the points

# Loop over all images and find checkerboard corners
obj_points, img_points = [], [] # Arrays to store object points and image points from all the images
fig, axes = plt.subplots(nrows=3, ncols=5, figsize=(15, 9))  # Create a figure with 3 rows and 5 columns of subplots
for i, image_path in enumerate(glob.glob('./Calibration_Imgs/*.jpg')):  # Loop over all images in the folder
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Convert the image to grayscale
    ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)  # Find the chessboard corners 
    if ret:
        obj_points.append(obj)
        img_points.append(corners)
        cv2.drawChessboardCorners(img, pattern_size, corners, ret)  # Draw the corners on the image
        
        # Calculate reprojection error for current image
        _, K, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)
        img_points2, _ = cv2.projectPoints(obj, rvecs[-1], tvecs[-1], K, dist)
        error = cv2.norm(corners, img_points2, cv2.NORM_L2) / len(img_points2)
        
        # Plot the image with the reprojection error
        row = i // 5
        col = i % 5
        ax = axes[row, col]
        ax.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        ax.set_title(f"Image {i+1}\nReprojection Error: {error:.4f}")
        ax.axis('off')
        
# Hide remaining subplots
for j in range(i+1, 15):
    row = j // 5
    col = j % 5
    axes[row, col].set_visible(False)
plt.show()

# Print the camera matrix
np.set_printoptions(suppress=True, precision=6)                # Set the print options to suppress scientific notation and print 6 decimal places
print(f"\nIntrinsic Matrix: \n{K}\n")