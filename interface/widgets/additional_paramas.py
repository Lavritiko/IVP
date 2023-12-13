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
        
        self.label_i        = CTkLabel(self.frame, text="i0")
        self.input_i        = CTkEntry(self.frame, width=50)
        self.input_i.insert(0, '0')

        self.label_j        = CTkLabel(self.frame, text="j0")
        self.input_j        = CTkEntry(self.frame, width=50)
        self.input_j.insert(0, '0')
        
        self.label_r        = CTkLabel(self.frame, text="Радиус")
        self.input_r        = CTkEntry(self.frame, placeholder_text='R', width=50)
        self.input_r.insert(0, '80')
        
        self.label_N        = CTkLabel(self.frame, text="Кол-во на сторону")
        self.input_N        = CTkEntry(self.frame, placeholder_text='N', width=50)
        self.input_N.insert(0, '5')

        self.label_a        = CTkLabel(self.frame, text="Длина стороны")
        self.input_a        = CTkEntry(self.frame, placeholder_text='a', width=50)
        self.input_a.insert(0, '50')

        self.label_D        = CTkLabel(self.frame, text="Расстояние")
        self.input_D        = CTkEntry(self.frame, placeholder_text='D', width=50)
        self.input_D.insert(0, '100')

        self.label_T        = CTkLabel(self.frame, text="Амплитуда колебания")
        self.input_T        = CTkEntry(self.frame, placeholder_text='T', width=50)
        self.input_T.insert(0, '10')
        
        self.label_delta  = CTkLabel(self.frame, text="Дельта")
        self.input_delta  = CTkEntry(self.frame, placeholder_text='delta', width=50)
        self.input_delta.insert(0, '80')

        self.label_frames      = CTkLabel(self.frame, text="Количество кадров")
        self.input_frames      = CTkEntry(self.frame, placeholder_text='frames', width=50)
        self.input_frames.insert(0, '200')

        self.label_t        = CTkLabel(self.frame, text="Время(сек)")
        self.input_t        = CTkEntry(self.frame, placeholder_text='t', width=50)
        self.input_t.insert(0, '10')


        self.frame.grid(row=4, column=0, sticky=NSEW, padx=10, pady=10, ipady=5)
        self.input_label.grid(row=0, column=0, sticky=NSEW, padx=10, pady=5)

    def forget(self):    
        self.label_i.grid_forget()
        self.input_i.grid_forget()

        self.label_j.grid_forget()
        self.input_j.grid_forget()

        self.label_r.grid_forget()
        self.input_r.grid_forget()
        
        self.label_N.grid_forget()
        self.input_N.grid_forget()

        self.label_a.grid_forget()
        self.input_a.grid_forget()

        self.label_D.grid_forget()
        self.input_D.grid_forget()

        self.label_T.grid_forget()
        self.input_T.grid_forget()

        self.label_delta.grid_forget()
        self.input_delta.grid_forget()

        self.label_frames.grid_forget()
        self.input_frames.grid_forget()

        self.label_t.grid_forget()
        self.input_t.grid_forget()

    def grid_impulse(self):
        self.input_label.configure(text="Введите координаты импульса:")

        self.label_i.grid(row=1, column=0, sticky=W, padx=10, pady=3)
        self.input_i.grid(row=1, column=1, sticky=W, padx=10, pady=3)

        self.label_j.grid(row=2, column=0, sticky=W, padx=10, pady=3)
        self.input_j.grid(row=2, column=1, sticky=W, padx=10, pady=3)
        
    
    def grid_hop(self):
        self.input_label.configure(text="Введите координаты скачка:")

        self.label_i.grid(row=1, column=0, sticky=W, padx=10, pady=3)
        self.input_i.grid(row=1, column=1, sticky=W, padx=10, pady=3)

        self.label_j.grid(row=2, column=0, sticky=W, padx=10, pady=3)
        self.input_j.grid(row=2, column=1, sticky=W, padx=10, pady=3)

    def grid_circle(self):
        self.input_label.configure(text="Введите координаты и радиус круга:")

        self.label_i.grid(row=1, column=0, sticky=W, padx=10, pady=3)
        self.input_i.grid(row=1, column=1, sticky=W, padx=10, pady=3)

        self.label_j.grid(row=2, column=0, sticky=W, padx=10, pady=3)
        self.input_j.grid(row=2, column=1, sticky=W, padx=10, pady=3)

        self.label_r.grid(row=3, column=0, sticky=W, padx=10, pady=3)
        self.input_r.grid(row=3, column=1, sticky=W, padx=10, pady=3)

        self.label_delta.grid(row=4, column=0, sticky=W, padx=10, pady=3)
        self.input_delta.grid(row=4, column=1, sticky=W, padx=10, pady=3)

        self.label_T.grid(row=5, column=0, sticky=W, padx=10, pady=3)
        self.input_T.grid(row=5, column=1, sticky=W, padx=10, pady=3)

        self.label_frames.grid(row=6, column=0, sticky=W, padx=10, pady=3)
        self.input_frames.grid(row=6, column=1, sticky=W, padx=10, pady=3)
        
        self.label_t.grid(row=7, column=0, sticky=W, padx=10, pady=3)
        self.input_t.grid(row=7, column=1, sticky=W, padx=10, pady=3)   

    def grid_square(self):       
        self.input_label.configure(text="Введите координаты и сторону квадрата:")
        
        self.label_i.grid(row=1, column=0, sticky=W, padx=10, pady=3)
        self.input_i.grid(row=1, column=1, sticky=W, padx=10, pady=3)

        self.label_j.grid(row=2, column=0, sticky=W, padx=10, pady=3)
        self.input_j.grid(row=2, column=1, sticky=W, padx=10, pady=3)
        
        self.label_a.grid(row=3, column=0, sticky=W, padx=10, pady=3)
        self.input_a.grid(row=3, column=1, sticky=W, padx=10, pady=3)

        self.label_delta.grid(row=4, column=0, sticky=W, padx=10, pady=3)
        self.input_delta.grid(row=4, column=1, sticky=W, padx=10, pady=3)
        
        self.label_T.grid(row=5, column=0, sticky=W, padx=10, pady=3)
        self.input_T.grid(row=5, column=1, sticky=W, padx=10, pady=3)

        self.label_frames.grid(row=6, column=0, sticky=W, padx=10, pady=3)
        self.input_frames.grid(row=6, column=1, sticky=W, padx=10, pady=3)
        
        self.label_t.grid(row=7, column=0, sticky=W, padx=10, pady=3)
        self.input_t.grid(row=7, column=1, sticky=W, padx=10, pady=3)
        
    def grid_chess(self):  
        self.input_label.configure(text="Введите кол-во клеток в ряду и сторону квадрата:")

        self.label_N.grid(row=1, column=0, sticky=W, padx=10, pady=3)
        self.input_N.grid(row=1, column=1, sticky=W, padx=10, pady=3)

        self.label_a.grid(row=2, column=0, sticky=W, padx=10, pady=3)
        self.input_a.grid(row=2, column=1, sticky=W, padx=10, pady=3)

    def grid_node_circles(self):
        self.input_label.configure(text="Введите кол-во кругов в ряду и их радиус:")

        self.label_N.grid(row=1, column=0, sticky=W, padx=10, pady=3)
        self.input_N.grid(row=1, column=1, sticky=W, padx=10, pady=3)

        self.label_r.grid(row=2, column=0, sticky=W, padx=10, pady=3)
        self.input_r.grid(row=2, column=1, sticky=W, padx=10, pady=3)

        self.label_D.grid(row=3, column=0, sticky=W, padx=10, pady=3)
        self.input_D.grid(row=3, column=1, sticky=W, padx=10, pady=3)

        self.label_frames.grid(row=4, column=0, sticky=W, padx=10, pady=3)
        self.input_frames.grid(row=4, column=1, sticky=W, padx=10, pady=3)
        
        self.label_t.grid(row=5, column=0, sticky=W, padx=10, pady=3)
        self.input_t.grid(row=5, column=1, sticky=W, padx=10, pady=3) 


    
    
