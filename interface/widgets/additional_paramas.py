from  customtkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import numpy as np


class AdditionalParamasFrame:
    def __init__(self, master):
        self.master = master

        self.frame = CTkFrame(self.master, corner_radius=5, fg_color=("gray10", "gray10"))
        self.input_label    = CTkLabel(self.frame, text=" ")
        
        self.input_i        = CTkEntry(self.frame, placeholder_text='i0', width=50)
        self.input_i.insert(0, '0')
        self.input_j        = CTkEntry(self.frame, placeholder_text='j0', width=50)
        self.input_j.insert(0, '0')
        self.input_r        = CTkEntry(self.frame, placeholder_text='R', width=70)
        self.input_r.insert(0, '0')
        self.input_N        = CTkEntry(self.frame, placeholder_text='кол-во', width=70)
        self.input_N.insert(0, '0')
        self.input_a        = CTkEntry(self.frame, placeholder_text='размер', width=70)
        self.input_a.insert(0, '0')
        
        self.frame.grid(row=4, column=0, sticky=NSEW, padx=10, pady=10, ipady=5)
        self.input_label.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

    def forget(self):
        self.input_i.grid_forget()
        self.input_j.grid_forget()
        self.input_r.grid_forget()
        self.input_N.grid_forget()
        self.input_a.grid_forget()

    def grid_impulse(self):
        self.input_label.configure(text="Введите координаты импульса:")
        self.input_i.grid(row=1, column=0, sticky=W, padx=10)

        self.input_j.grid(row=1, column=0, padx=10)
        
    
    def grid_hop(self):
        self.input_label.configure(text="Введите координаты скачка:")
        self.input_i.grid(row=1, column=0, sticky=W, padx=10)
        self.input_j.grid(row=1, column=0, padx=10)

    def grid_circle(self):
        self.input_label.configure(text="Введите координаты и радиус круга:")
        self.input_i.grid(row=1, column=0, sticky=W, padx=10)
        self.input_j.grid(row=1, column=0, padx=10)
        self.input_r.grid(row=2, column=0, sticky=W, padx=10, pady=5)
        

    def grid_square(self):       
        self.input_label.configure(text="Введите координаты и сторону квадрата:")
        self.input_i.grid(row=1, column=0, sticky=W, padx=10)
        self.input_j.grid(row=1, column=0, padx=10)
        self.input_a.grid(row=2, column=0, sticky=W, padx=10, pady=5)
        
    def grid_chess(self):  
        self.input_label.configure(text="Введите колиество клеток в ряду и сторону квадрата:")
        self.input_N.grid(row=1, column=0, sticky=W, padx=10)
        self.input_a.grid(row=1, column=0, padx=10)


    
    
