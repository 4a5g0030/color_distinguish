import cv2
import numpy as np
import color_distinguish as cd


def mark_color(image, c_th):
    c_th = c_th
    image = image
    mark_img = cd.color_distinguish(image)
    color_box = {'R': 0, 'G': 0, 'B': 0}

    # finding the range of red,blue and yellow color in the image
    red = mark_img.res_red()
    blue = mark_img.res_blue()
    green = mark_img.res_green()

    # Morphological transformation, Dilation
    kernal = np.ones((9, 9), 'uint8')

    red = cv2.dilate(red, kernal)
    res = cv2.bitwise_and(image, image, mask=red)

    blue = cv2.dilate(blue, kernal)
    res1 = cv2.bitwise_and(image, image, mask=blue)

    green = cv2.dilate(green, kernal)
    res2 = cv2.bitwise_and(image, image, mask=green)

    contours, hierarchy = cv2.findContours(
        red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > c_th:
            color_box['R'] += 1
            x, y, w, h = cv2.boundingRect(contour)
            image = cv2.rectangle(
                image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(image, "RED color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    contours, hierarchy = cv2.findContours(
        green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > c_th:
            color_box['G'] += 1
            x, y, w, h = cv2.boundingRect(contour)
            image = cv2.rectangle(
                image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, "GREEN color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))

    contours, hierarchy = cv2.findContours(
        blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area > c_th:
            color_box['B'] += 1
            x, y, w, h = cv2.boundingRect(contour)
            image = cv2.rectangle(
                image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(image, "BLUE color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

    return image, color_box
