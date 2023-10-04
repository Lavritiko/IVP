import cv2
import numpy as np

class Settings:
    def __init__(self):
        pass

    def gray(self, img):
        gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return gray_img
