from  customtkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import numpy as np

class ModelCreatingWindow():
    def __init__(self, parent, title):
        self.root = CTkToplevel(parent)
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.title(title)
        self.root.grab_set()
        # self.root.grid_rowconfigure(0, weight=1)
        # self.root.grid_columnconfigure(1, weight=1)

        self.model_possible_functionality: dict = {
             'Задержанный единичный импульс': self.delayed_single_impulse,
             'Задержанный единичный скачок': self.delayed_single_hop,
             'Одиночный круг': self.single_circle,
             'Одиночный квадрат': self.single_square,
             'Шахматная доска': self.chessboard,
             'Круги в узлах прямоугольной решетки': self.circles_at_nodes,
             'Случайные круги': self.random_circles,
             'Белый шум с равномерным распределением': self.noise_uniform_distribution,
             'Белый шум с нормальным распределением': self.noise_normal_distribution,
             'Плоская гравитационная волна': self.flat_gravitational_wave,
        }
        self.model_var = StringVar(value="Choose a model")
        

        ##########create frame 1###########
        self.size_input_frame = CTkFrame(self.root)
        self.size_input_label = CTkLabel(self.size_input_frame, text="Введите размер модели")
        self.size_input_x = CTkEntry(self.size_input_frame, placeholder_text='X', width=70)
        self.size_input_y = CTkEntry(self.size_input_frame, placeholder_text='Y', width=70)

        #########create frame 2############
        self.model_input_frame = CTkFrame(self.root)
        self.model_input_label = CTkLabel(self.model_input_frame, text="Выберите функциональность модели")
        self.model_option = CTkOptionMenu(self.model_input_frame, values=[*self.model_possible_functionality.keys()], variable=self.model_var, command=self.model_input_callback, width=350)


        #########create frame 3############
        self.additional_input_frame = CTkFrame(self.root)
        self.additional_input_label = CTkLabel(self.additional_input_frame, text="Дополнительные параметры")
        self.input_label = CTkLabel(self.additional_input_frame, text=" ")
        self.input_i = CTkEntry(self.additional_input_frame, placeholder_text='i0', width=70)
        self.input_j = CTkEntry(self.additional_input_frame, placeholder_text='j0', width=70)
        self.input_r = CTkEntry(self.additional_input_frame, placeholder_text='R', width=70)
        self.input_N = CTkEntry(self.additional_input_frame, placeholder_text='кол-во клеток', width=70)
        self.input_a = CTkEntry(self.additional_input_frame, placeholder_text='размер клетки', width=70)


        self.draw_widgets()
    def draw_widgets(self):
        
        ################# 1 блок. Размер изображения ###########################

        self.size_input_frame.pack(side=TOP, fill=X, pady=10)
        self.size_input_label.pack(anchor= NW, padx=10)
        self.size_input_x.pack(side=LEFT, padx=10)
        self.size_input_y.pack(side=LEFT, padx=10)
        
        ################ 2 блок. Вид модели ####################################

        self.model_input_frame.pack(side=TOP, fill=X, pady=10)
        self.model_input_label.pack(anchor= NW, padx=10)
        self.model_option.pack(side=LEFT, padx=10)

        ################ 3 блок. Дополнительные параметры ####################################

        self.additional_input_frame.pack(side=TOP, fill=X, pady=10)
        self.additional_input_label.pack(anchor=NW, padx=10)
        self.input_label.pack(anchor=NW, padx=10)


    def model_input_callback(self, choice):
        self.model_possible_functionality[choice]()
    
    def delayed_single_impulse(self):
        
        self.input_label.configure(text="Введите координаты импульса:")
                
        self.input_i.pack(side=LEFT, padx=10)
        self.input_j.pack(side=LEFT, padx=10)
    
    def delayed_single_hop(self):
        self.input_label.configure(text="Введите координаты скачка:")
        
        self.input_label.pack(anchor=NW, padx=10)
        self.input_i.pack(side=LEFT, padx=10)
        self.input_j.pack(side=LEFT, padx=10)
        
    
    def single_circle(self):
         self.input_label.configure(text="Введите параметры круга:")
         self.input_i.pack(side=LEFT, padx=10)
         self.input_j.pack(side=LEFT, padx=10)


    def single_square(self):
        self.input_label.configure(text="Введите параметры квадрата:")
        self.input_i.pack(side=LEFT, padx=10)
        self.input_j.pack(side=LEFT, padx=10)
    
    def chessboard(self):
        self.input_N.pack(side=LEFT, padx=10)
        self.input_a.pack(side=LEFT, padx=10)
    
    def circles_at_nodes(self):
         pass
    
    def random_circles(self):
         pass
    
    def noise_uniform_distribution(self):
         pass
    
    def noise_normal_distribution(self):
         pass
    
    def flat_gravitational_wave(self):
         pass