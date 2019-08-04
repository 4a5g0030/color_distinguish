import cv2
import numpy as np
import color_distinguish as cd

path = 'test_data\RGB.png'
image = cv2.imread(path)
mark_img = cd.color_distinguish(image)

# finding the range of red,blue and yellow color in the image
red = mark_img.res_red()
blue = mark_img.res_blue()
green = mark_img.res_green()

# Morphological transformation, Dilation
kernal = np.ones((5, 5), 'uint8')

red = cv2.dilate(red, kernal)
res = cv2.bitwise_and(image, image, mask = red)

blue = cv2.dilate(blue, kernal)
res1 = cv2.bitwise_and(image, image, mask = blue)

green = cv2.dilate(green, kernal)
res2 = cv2.bitwise_and(imshow, imshow, mask = green)
