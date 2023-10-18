from  customtkinter import *
import cv2
from PIL import Image
from PIL import ImageTk

class Output_display:
    def __init__(self, place=None):
        self.place = place
        # self.img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # self.img = Image.fromarray(self.img)
        # self.img = ImageTk.PhotoImage(self.img)

    def cv_to_pil(self, image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)

        return img

    def draw_picture(self, image):
        img = self.cv_to_pil(image)
        self.label = CTkLabel(self.place)
        self.label.configure(image=img, text='')
        self.label.image=img
        self.label.pack()
    
    def on_change(self, image):
        img = self.cv_to_pil(image)
        self.label.configure(image=img)
        self.label.image=img
