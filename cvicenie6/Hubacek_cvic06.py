import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img1 = np.zeros((200, 200), np.uint8)


cv.rectangle(img1, (0, 100), (200, 200), (255), -1)  # White rectangle
cv.rectangle(img1, (0, 50), (100, 150), (125), -1)  # Gray rectangle
cv.rectangle(img1, (80, 60), (125, 120), (100), -1) # Dark gray rectangle
cv.rectangle(img1, (120, 30), (20, 60), (200), -1)  # Dark gray rectangle

plt.imshow(img1, "gray")


img2  = np.flip(img1)
plt.imshow(img2, 'gray')

# plt.subplot(3,1,1)
# plt.title("Example")
# plt.imshow(img1, 'gray')
# plt.hist(img1.ravel(), 256, [0, 256]) #ravel / konverzia 2D do 1D pola

# plt.tight_layout()
# plt.savefig("Example.png")


plt.show()
