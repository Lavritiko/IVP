from  customtkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import numpy as np
from interface.widgets.additional_paramas import AdditionalParamasFrame

class ModelCreatingWindow():
    def __init__(self, parent, title):
        self.root = CTkToplevel(parent)
        self.root.geometry("1030x525")
        self.root.resizable(False, False)
        self.root.title(title)
        self.root.grab_set()
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

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
        
        self.modeling_frame = CTkFrame(self.root, corner_radius=0)
        self.modeling_frame.grid(row=0, column=0, sticky=NSEW)
        self.modeling_frame.grid_rowconfigure(6, weight=1)

        self.modeling_frame_label = CTkLabel(self.modeling_frame, text="Моделирование",
                                             compound='left', font=CTkFont(size=15, weight='bold'))
        self.modeling_frame_label.grid(row=0, column=0, pady=20)

        # ##########create frame 1.1###########
        self.size_input_frame = CTkFrame(self.modeling_frame_label, corner_radius=5, fg_color=("gray10", "gray10"))
        self.size_input_label = CTkLabel(self.size_input_frame, text="Введите размер модели")
        self.size_input_x = CTkEntry(self.size_input_frame, placeholder_text='X', width=50)
        self.size_input_y = CTkEntry(self.size_input_frame, placeholder_text='Y', width=50)

        # #########create frame 1.2############
        self.model_input_frame = CTkFrame(self.modeling_frame_label, corner_radius=5, fg_color=("gray10", "gray10"))
        self.model_input_label = CTkLabel(self.model_input_frame, text="Выберите модель")
        self.model_option = CTkOptionMenu(self.model_input_frame, values=[*self.model_possible_functionality.keys()], variable=self.model_var, command=self.model_input_callback, width=325)


        # #########create frame 1.3############
        self.additional_input_frame = AdditionalParamasFrame(self.modeling_frame_label)

        self.additional_input_label = CTkLabel(self.modeling_frame_label, text="Дополнительные параметры", font=CTkFont(size=13, weight='bold'))

        self.model_button = CTkButton(self.modeling_frame, text="Смоделировать", command=self.model_button_callback)

        ###########create frame 2.1#############
        self.preview_frame = CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.preview_frame.grid(row=0, column=1, sticky=NSEW)
        self.preview_frame.grid_columnconfigure(0, weight=4)


        self.previw_label = CTkLabel(self.preview_frame, text="Предварительный просмотр",
                                             font=CTkFont(size=15, weight='bold'))
        self.previw_label.grid(row=0, column=0, pady=20)

        self.preview_canvas = CTkCanvas(self.preview_frame, width=350, height=350, background='gray22')
        self.preview_canvas.grid(row=1, column=0, pady=20)

        self.accept_button = CTkButton(self.preview_frame, text="Принять", command=self.accept_button_callback)
        self.accept_button.grid(row=2, column=0, pady=10, padx=20, sticky=SE)


        self.draw_widgets()
        

    def draw_widgets(self):
        
        ################# 1 блок. Размер изображения ###########################


        self.size_input_frame.grid(row=1, column=0, sticky=NSEW, padx=10, pady=10, ipady=5)
        self.size_input_frame.grid_columnconfigure(0, minsize=200)
        self.size_input_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        self.size_input_x.grid(row=1, column=0, sticky=W, padx=10)
        self.size_input_y.grid(row=1, column=0, padx=10)
        
        ################ 2 блок. Вид модели ####################################

        self.model_input_frame.grid(row=2, column=0, sticky=NSEW, padx=10, pady=10, ipady=5)
        self.model_input_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        self.model_option.grid(row=1, column=0, sticky=NSEW, padx=10)
        

        ################ 3 блок. Дополнительные параметры ####################################

        self.additional_input_label.grid(row=3, column=0, sticky=W, padx=10, pady=5)

        self.model_button.grid(row=5, column=0, sticky=SE, padx=10, pady=35)

    def model_input_callback(self, choice):
        self.model_possible_functionality[choice]()

    def model_button_callback(self):
        pass
    
    def accept_button_callback(self):
        pass
    
    def delayed_single_impulse(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_impulse()
    
    def delayed_single_hop(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_hop()

    def single_circle(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_circle()

    def single_square(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_square()
    
    def chessboard(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_chess()
    
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