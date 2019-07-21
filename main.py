import cv2
import color_distinguish as cd
import matplotlib.pyplot as plt


def main():
    img = cv2.imread('test_data/RGB.png')
    color = cd.color_distinguish(img)
    color = color.res_blue()

    cv2.imshow('img', color)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
