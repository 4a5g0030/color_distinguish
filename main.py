import cv2
import color_distinguish as cd
import matplotlib.pyplot as plt
import mark_color as mc


def main():
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.GaussianBlur(frame, (5, 5), 1.5)
        frame = mc.mark_color(frame, 3000)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def t_one():
    img = cv2.imread('test_data/RGB.png')
    img = mc.mark_color(img, 300)
    cv2.imshow('img', img)
    cv2.waitKey(0)


def t_tow():
    img = cv2.imread('test_data/test_myroom.jpg')
    img = mc.mark_color(img, 5000)
    cv2.imshow('img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
