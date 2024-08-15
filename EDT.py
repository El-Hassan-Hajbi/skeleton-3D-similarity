import numpy as np
from scipy.ndimage import distance_transform_edt

def get_EDT(img):
    return distance_transform_edt(img==0)

def central_difference_gradient(image):
  """
  Calculates the gradient of a 3D image using the central difference method.

  Args:
      image: A 3D array representing the image.

  Returns:
      A tuple containing the 3D gradients for each axis (dx, dy, dz).
  """

  # Get image dimensions
  x_dim, y_dim, z_dim = image.shape

  # Create empty arrays for gradients in each direction
  dx = np.zeros_like(image)
  dy = np.zeros_like(image)
  dz = np.zeros_like(image)

  # Calculate gradients (excluding edges where necessary)
  for i in range(1, x_dim - 1):
    for j in range(1, y_dim - 1):
      for k in range(1, z_dim - 1):
        # Calculate central differences
        dx[i, j, k] = (image[i + 1, j, k] - image[i - 1, j, k]) / 2
        dy[i, j, k] = (image[i, j + 1, k] - image[i, j - 1, k]) / 2
        dz[i, j, k] = (image[i, j, k + 1] - image[i, j, k - 1]) / 2

  return dx, dy, dz

if __name__ == "__main__":

    a = np.zeros((10,10,10), dtype=np.int32) # try ones too 

    D = get_EDT(a)
    gradD = central_difference_gradient(D)
    print(np.array([gradD[0][1,1,1], gradD[1][1,1,1], gradD[2][1,1,1]]))