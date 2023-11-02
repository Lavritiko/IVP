import cv2
import numpy as np

class GraySettings:
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
        
        print(1111)

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

    
class Gray:
    def __init__(self,):
        self.beta_cnt = 30
        self.alpha_br = 50

        self.brightness = 0
        self.contrast = 0
        self.red = 0
        self.green = 0
        self.blue = 0
        
    def hmm2(self, img):
        blue_channel, green_channel, red_channel = cv2.split(img)

        blue_channel = ( red_channel * self.blue / 127 ) + self.blue # (1 + val / 127) * r
        green_channel = red_channel * self.green / 127 + self.green
        red_channel = red_channel * self.red / 127 + self.red

        blue_channel = np.uint8(np.clip(blue_channel, 0, 255))
        green_channel = np.uint8(np.clip(green_channel, 0, 255))
        red_channel = np.uint8(np.clip(red_channel, 0, 255))

        img = cv2.merge((blue_channel, green_channel, red_channel))

        img = img * (self.beta_cnt / 127 + 1) - self.beta_cnt + self.alpha_br
        img = np.uint8(np.clip(img, 0, 255))
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray_img
