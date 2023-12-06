import cv2 as cv
from  customtkinter import *
from PIL import Image, ImageTk
import numpy as np

class PreviewScreen():
    def __init__(self, master):
        pust = cv.imread('interface/img/no_image.png')
        self.img             = pust
        self.video           = None
        self.images          = []
        self.master          = master
        self.weight, self.height = pust.shape[1], pust.shape[0]
        self.play            = False
        self.t               = 0
        self.root            = CTkCanvas(self.master, height=350, width=350, background='gray22')
        self.image_creation()
        self.image_on_canvas = self.root.create_image(175, 175, anchor='center', image=self.photo)
        self.update()

    def image_creation(self):
        ratio = self.weight / self.height
        if self.height > self.weight:
            self.new_hight = 350
            self.new_width = int(self.new_hight * ratio)
        else:
            self.new_width = 350
            self.new_hight = int(self.new_width / ratio)

        self.image = Image.fromarray(self.img)
        self.image = self.image.resize((self.new_width, self.new_hight), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image=self.image)           

    def grid(self, row=1, column=0, pady=20):
        self.root.grid(row = row, column = column, pady = pady)

    def update(self):
        if self.play:
            if not self.images:
                self.read()

            #next image
            self.t += 1

            #return to first image
            if self.t >= len(self.images):
                self.t = 0

            #change image
            self.root.itemconfig(self.image_on_canvas, image=self.images[self.t])
            self.root.after(1000, self.update)
        else:
            self.image_creation()
            self.root.itemconfig(self.image_on_canvas, image=self.photo)

    def read(self):
        for frame in self.video:
            self.img = frame
            self.image_creation()
            self.images.append(self.photo)
            print(len(self.images))
