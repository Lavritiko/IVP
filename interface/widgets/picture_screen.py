from  customtkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
from settings.rgb_bw import gray
import numpy as np

class Output_display():
    def __init__(self, place, image_cv, conversion_func=None):
        self.conversion_func = conversion_func
        self.image_cv = image_cv
        self.image = image_cv
        self.place = place

        self.picture = CTkCanvas(self.place, height=image_cv.shape[0], width=image_cv.shape[1])
        self.picture.configure(background='gray22')
        
        self.is_gray = False
        self.br, self.cnt, self.r, self.g, self.b = 0, 0, 0, 0, 0

        self.cv_to_pil()

    def cv_to_pil(self):
        if self.is_gray:
            self.image = gray(self.image_cv, self.br, self.cnt, self.r, self.g, self.b)
            if self.conversion_func is not None:
                self.image = self.conversion_func(self.image)
        else:
            self.image = self.image_cv
            self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.image))
        self.picture.create_image(0, 0, image=self.photo, anchor=NW)
    
    def pack(self):
        self.picture.pack()
    
    def on_change(self):
        self.cv_to_pil()
