import cv2
import numpy as np
import color_distinguish as cd


def mark_color(image, c_th):
    c_th = c_th
    image = image
    mark_img = cd.color_distinguish(image)
    red_area, green_area, blue_area = 0, 0, 0
    color_box = [0, 0, 0]

    # finding the range of red,blue and yellow color in the image
    red = mark_img.res_red()
    blue = mark_img.res_blue()
    green = mark_img.res_green()

    # Morphological transformation, Dilation
    kernal = np.ones((9, 9), 'uint8')

    red = cv2.dilate(red, kernal)

    blue = cv2.dilate(blue, kernal)

    green = cv2.dilate(green, kernal)

    contours, hierarchy = cv2.findContours(
        red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        red_contour = max(contours, key=cv2.contourArea)
        red_area = cv2.contourArea(red_contour)

    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if area > c_th:
    #         color_box['R'] += 1
    #         x, y, w, h = cv2.boundingRect(contour)
    #         image = cv2.rectangle(
    #             image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #         cv2.putText(image, "RED color", (x, y),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    contours, hierarchy = cv2.findContours(
        green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        green_contour = max(contours, key=cv2.contourArea)
        green_area = cv2.contourArea(green_contour)

    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if area > c_th:
    #         color_box['G'] += 1
    #         x, y, w, h = cv2.boundingRect(contour)
    #         image = cv2.rectangle(
    #             image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #         cv2.putText(image, "GREEN color", (x, y),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))

    contours, hierarchy = cv2.findContours(
        blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        blue_contour = max(contours, key=cv2.contourArea)
        blue_area = cv2.contourArea(blue_contour)

    # for pic, contour in enumerate(contours):
    #     area = cv2.contourArea(contour)
    #     if area > c_th:
    #         color_box['B'] += 1
    #         x, y, w, h = cv2.boundingRect(contour)
    #         image = cv2.rectangle(
    #             image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #         cv2.putText(image, "BLUE color", (x, y),
    #                     cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

    max_area = max(red_area, green_area, blue_area)
    if max_area > c_th:
        if max_area == red_area:
            color_box[0] += 1
            x, y, w, h = cv2.boundingRect(red_contour)
            image = cv2.rectangle(
                image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(image, "RED color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
        elif max_area == green_area:
            color_box[1] += 1
            x, y, w, h = cv2.boundingRect(green_contour)
            image = cv2.rectangle(
                image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, "GREEN color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0))
        elif max_area == blue_area:
            color_box[2] += 1
            x, y, w, h = cv2.boundingRect(blue_contour)
            image = cv2.rectangle(
                image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(image, "BLUE color", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

    return image, color_box
