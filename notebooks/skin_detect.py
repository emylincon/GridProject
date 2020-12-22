''''| Author: Jean Vitor de Paulo
	| Date: 29/09/2018
	| https://github.com/Jeanvit/PySkinDetection
'''

import cv2
import numpy as np
import os
import sys
import time


class SkinDetector(object):

    # class constructor
    def __init__(self, imageName, saveName):
        self.image = cv2.imread(imageName)
        self.save_name = saveName
        if self.image is None:
            print("IMAGE NOT FOUND")
            exit(1)
        # print('res = ', cv2.resize(self.image, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)) #self.image = cv2.resize(self.image,(600,600),cv2.INTER_AREA)

        self.HSV_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        self.YCbCr_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2YCR_CB)
        self.binary_mask_image = self.HSV_image

    # ================================================================================================================================
    # function to process the image and segment the skin using the HSV and YCbCr colorspaces, followed by the Watershed algorithm
    def find_skin(self):
        self.__color_segmentation()
        self.__region_based_segmentation()

    # ================================================================================================================================
    # Apply a threshold to an HSV and YCbCr images, the used values were based on current research papers along with some
    # empirical tests and visual evaluation
    def __color_segmentation(self):
        lower_HSV_values = np.array([0, 40, 0], dtype="uint8")
        upper_HSV_values = np.array([25, 255, 255], dtype="uint8")

        lower_YCbCr_values = np.array((0, 138, 67), dtype="uint8")
        upper_YCbCr_values = np.array((255, 173, 133), dtype="uint8")

        # A binary mask is returned. White pixels (255) represent pixels that fall into the upper/lower.
        mask_YCbCr = cv2.inRange(self.YCbCr_image, lower_YCbCr_values, upper_YCbCr_values)
        mask_HSV = cv2.inRange(self.HSV_image, lower_HSV_values, upper_HSV_values)

        self.binary_mask_image = cv2.add(mask_HSV, mask_YCbCr)

    # ================================================================================================================================
    # Function that applies Watershed and morphological operations on the thresholded image
    def __region_based_segmentation(self):
        # morphological operations
        image_foreground = cv2.erode(self.binary_mask_image, None, iterations=3)  # remove noise
        dilated_binary_image = cv2.dilate(self.binary_mask_image, None,
                                          iterations=3)  # The background region is reduced a little because of the dilate operation
        ret, image_background = cv2.threshold(dilated_binary_image, 1, 128,
                                              cv2.THRESH_BINARY)  # set all background regions to 128

        image_marker = cv2.add(image_foreground,
                               image_background)  # add both foreground and backgroud, forming markers. The markers are "seeds" of the future image regions.
        image_marker32 = np.int32(image_marker)  # convert to 32SC1 format

        cv2.watershed(self.image, image_marker32)
        m = cv2.convertScaleAbs(image_marker32)  # convert back to uint8

        # bitwise of the mask with the input image
        ret, image_mask = cv2.threshold(m, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        output = cv2.bitwise_and(self.image, self.image, mask=image_mask)

        # save the image
        self.save_image(output)

    # ================================================================================================================================
    def save_image(self, image):
        cv2.imwrite(self.save_name, image)


def run():
    base_dir = r'E:\Pycharm Projects\GridProject\data\dataset\train'
    output_dir = r'E:\Pycharm Projects\GridProject\data\skin_detect'
    for dir_ in os.listdir(base_dir):
        print(f'running for {dir_}')
        for image in os.listdir(fr'{base_dir}\{dir_}'):
            SkinDetector(imageName=fr'{base_dir}\{dir_}\{image}', saveName=fr'{output_dir}\{dir_}\{image}').find_skin()
            name = fr'{dir_}\{image}'
            sys.stdout.write(f"\rDone {name}")
            sys.stdout.flush()


run()