"""
    Họ tên: Đinh Ngọc Vân
    MSSV: 19021390
    Lớp: INT3404_20
"""

import cv2
import numpy
import numpy as cp


def q_0():
    img = cv2.imread('apple.png')
    cv2.imwrite('new_apple.png', img)
    cv2.imshow('Picture ', img)
    # cv2.waiKey(a): Chờ a miliseconds để tắt cửa sổ. Trong trường hợp a = 0, sẽ hiện cửa sổ tĩnh không tự tắt cho đến khi bấm phím.
    cv2.waitKey(0)


def q_1():
    # openCV luôn sử dụng thứ tự kênh Blue - Green - Red (BGR)
    img = cv2.imread('chromatic_aberration.png')
    height, width = img.shape[:2]
    print("height", height, "width", width)

    YCbCrcolor = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    print("YCbCr Blue: ", numpy.average(YCbCrcolor[:, :, 0]), "YCbCr Green: ", numpy.average(
        YCbCrcolor[:, :, 1]), "YCbCr Red: ", numpy.average(YCbCrcolor[:, :, 2]))

    RBGColor = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print("RBG Blue: ", numpy.average(RBGColor[:, :, 0]), "RBG Green: ", numpy.average(
        RBGColor[:, :, 1]), "RBG Red: ", numpy.average(RBGColor[:, :, 2]))


def q_2():
    # original height = 489, width = 652
    img = cv2.imread('apple.png')
    clear_apple = img[300:475, 362:540]
    cv2.imwrite('clear_apple.jpg', clear_apple)
    cv2.imshow('Clear Apple picture:', clear_apple)

    blurred_apple = img[38:124, 90:176]
    cv2.imwrite('blurred_apple.jpg', blurred_apple)
    cv2.imshow('Blurred Apple picture:', blurred_apple)
    cv2.waitKey(0)


def q_3(limit):
    img = cv2.imread('font.png')
    original = img
    height, width = original.shape[:2]
    dim = (width, height)
    grayColor = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
    i = 1
    # set giới hạn là limit
    # Sau khi downsampling, độ phân giải ảnh giảm, ảnh mờ đi tỉ lệ thuận với độ giảm của kích thước ảnh,
    # Độ chi tiết ảnh sau khi downsampling so với ảnh ban đầu giảm đi theo độ giảm kích thước ảnh.
    while i > limit:
        img = cv2.pyrDown(img)
        i = i / 2
        print(img.shape, "  ")
        cv2.imshow("New_pic", img)
        cv2.waitKey(0)

    reImg = cv2.resize(img, dim)
    cv2.imshow("Resize", reImg)
    cv2.waitKey(0)
    pSNR = cv2.PSNR(original, reImg)
    print(pSNR)

    # Hình ảnh quá táo mờ là do hiệu ứng làm mờ(blur) gây ra
    # Một số cách làm ảnh sắc nét: Bộ lọc: filter2D. Bộ lọc làm mịn: Gaussian


if __name__ == "__main__":
    # q_0()
    q_1()
    # q_2()
    q_3(0.1)
