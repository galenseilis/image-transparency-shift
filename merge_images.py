from skimage import io
import numpy as np
from cv2 import resize
import matplotlib.pyplot as plt

left = np.rot90(io.imread('left.jpg'))
left = resize(left, (1080, 1920))
right = resize(np.rot90(io.imread('right.JPG')), left.shape[0:-1][::-1])

for j in range(left.shape[0]):
    new_img = np.zeros(left.shape)
    for i in range(left.shape[0]):
        right_weight = 1 - np.abs(j - i % left.shape[0]) / left.shape[0]
        left_weight = 1 - right_weight
        new_img[i] = left_weight * left[i] + right_weight * right[i]

    num = str(j).zfill(4)
    io.imsave(f'new_img_{num}.jpg', np.rot90(np.rot90(np.rot90(new_img/255))))
    print(num)
