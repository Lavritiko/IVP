import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

IS_UPDATE_FUCKING_STATISTICS = [False]

class Settings:
    def __init__(self, img):
        
        self.img = img
        self.img2 = img
        self.alpha_br = 50
        self.beta_cnt = 30

    def gray(self):

        gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        return gray_img
    
    
    def brightness(self, value):

        self.img = self.img2 * (self.beta_cnt / 127 + 1) - self.beta_cnt + value
        self.img = np.uint8(np.clip(self.img, 0, 255))
        self.alpha_br = value

        return self.img
        
    def contrast(self, value):

        self.img = self.img2 * (value / 127 + 1) - value + self.alpha_br
        self.img = np.uint8(np.clip(self.img, 0, 255))
        self.beta_cnt = value

        return self.img

    def red(self, value):
        b, g, r = cv2.split(self.img2)
        r = r * value / 127 + value
        r = np.uint8(np.clip(r, 0, 255))
        self.img = cv2.merge((b, g, r))
        
        return self.img
    
    def blue(self, value):
        b, g, r = cv2.split(self.img2)
        b = b * value / 127 + value
        b = np.uint8(np.clip(b, 0, 255))
        self.img = cv2.merge((b, g, r))
        
        return self.img
    
    def green(self, value):
        b, g, r = cv2.split(self.img2)
        g = g * value / 127 + value
        g = np.uint8(np.clip(g, 0, 255))
        self.img = cv2.merge((b, g, r))
        
        return self.img

    
def gray(img, alpha_br, beta_cnt, red, green, blue):
    blue_channel, green_channel, red_channel = cv2.split(img)

    v = blue / 127
    chan = blue_channel
    sig = np.sign(blue)
    blue_channel =  chan + (1 + sig) / 2 * v * (255 - chan) + \
                         + (1 - sig) / 2 * v * chan
                         
    v = green / 127
    chan = green_channel
    sig = np.sign(green)
    green_channel = chan + (1 + sig) / 2 * v * (255 - chan) + \
                         + (1 - sig) / 2 * v * chan
                         
    v = red / 127
    chan = red_channel
    sig = np.sign(red)
    red_channel =   chan + (1 + sig) / 2 * v * (255 - chan) + \
                         + (1 - sig) / 2 * v * chan

    blue_channel = np.uint8(np.clip(blue_channel, 0, 255))
    green_channel = np.uint8(np.clip(green_channel, 0, 255))
    red_channel = np.uint8(np.clip(red_channel, 0, 255))

    img = cv2.merge((blue_channel, green_channel, red_channel))

    img = img * (beta_cnt / 127 + 1) - beta_cnt + alpha_br
    img = np.uint8(np.clip(img, 0, 255))
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img

def image_statistics(img):
    mean, std_dev = cv2.meanStdDev(img)
    kurt = kurtosis(img, axis=None)
    skewness = skew(img, axis=None)
    minimum = np.min(img)
    maximum = np.max(img)
    quantile5 = np.quantile(img, .05)
    quantile95 = np.quantile(img, .95)
    return mean[0, 0], std_dev[0, 0], kurt, skewness, minimum, maximum, quantile5, quantile95



