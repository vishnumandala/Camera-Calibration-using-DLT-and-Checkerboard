import numpy as np

# Define the image points and world points
image_points = np.array([[757, 213], [758, 415], [758, 686], [759, 966], [1190, 172], [329, 1041], [1204, 850], [340, 159]])
world_points = np.array([[0, 0, 0], [0, 3, 0], [0, 7, 0], [0, 11, 0], [7, 1, 0], [0, 11, 7], [7, 9, 0], [0, 1, 7]])

# Step 1: Direct Linear Transformation (DLT) algorithm
def dlt(image_points, world_points):
    A = []                                                          # Initialize an empty list to hold the A matrix
    for i, (X, Y, Z) in enumerate(world_points):
        x, y = image_points[i]
        A.append([X, Y, Z, 1, 0, 0, 0, 0, -x*X, -x*Y, -x*Z, -x])    # Append the first row of the ith pair of points inclusive of the homogenous coordinate
        A.append([0, 0, 0, 0, X, Y, Z, 1, -y*X, -y*Y, -y*Z, -y])    # Append the second row of the ith pair of points inclusive of the homogenous coordinate
    A = np.asarray(A)                                               # Convert A to a numpy array

    # Solve for P using SVD
    _, _, V = np.linalg.svd(A)
    P = V[-1, :].reshape((3, 4))

    return P

# Step 2: Decompose P matrix using Gram-Schmidt process
def gram_schmidt(P):
    M = P[:3, :3].copy()                                        # Extract the 3x3 matrix M from P

    a1, a2, a3 = M[0,:], M[1,:], M[2,:]                      # Extract the first, second, and third rows of M
    e3 = a3 / np.linalg.norm(a3)                              # Compute the third row of the rotation matrix R
    p2 = np.dot(e3, a2) * e3                                  # Compute the second row of the rotation matrix R
    e2 = (a2 - p2) / np.linalg.norm(a2 - p2)                  
    p1 = np.dot(e2, a1) * e2 + np.dot(e3, a1) * e3            # Compute the first row of the rotation matrix R
    e1 = (a1 - p1) / np.linalg.norm(a1 - p1)                  
    R = np.row_stack((e1, e2, e3))                            # Compute the rotation matrix R using the Gram-Schmidt process
    
    K = M @ np.linalg.inv(R)                                 # Compute the intrinsic matrix K    
    K /= K[-1, -1]                                          # Normalize the intrinsic matrix K                             
    t= (np.linalg.inv(K) @ P[:, -1]).reshape((3, 1))            # Compute the translation vector t by solving for the last column of P

    return K, R, t

# Step 3: Compute reprojection error for each point
def reprojection_error(image_points, world_points, P):
    for i, (X, Y, Z) in enumerate(world_points):
        p = P @ np.array([X, Y, Z, 1])                          # Compute the projection of the ith point in world coordinates
        p /= p[-1]                                              # Normalize the projection
        error = np.linalg.norm(image_points[i] - p[:2])         # Compute the reprojection error
        print(f"Reprojection Error for Point {i+1} is: {error}")

P = dlt(image_points, world_points)
K, R, t = gram_schmidt(P)

np.set_printoptions(suppress=True, precision=6)                # Set the print options to suppress scientific notation and print 6 decimal places
print("\nProjection Matrix (P):\n", P, "\n\nIntrinsic Matrix (K):\n", K, "\n\nRotation Matrix (R):\n", R, "\n\nTranslation Vector (t):\n", t, "\n")
reprojection_error(image_points, world_points, P)
print('\n')