from  customtkinter import *
import tkinter as tk
from interface.widgets.switch_widget import MySwitch
from interface.widgets.picture_screen import Output_display
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ConversionFunctions:
    def __init__(self, master = None, preview_frame=None) -> None:
        if master is None:
            master = CTk()
        
        self.master = master
        self.preview_frame = preview_frame
        
        self.functions_frame        = CTkFrame(self.master)
        
        self.is_inversion           = StringVar(value='0')
        self.inversion_switch       = MySwitch(self.functions_frame,
                                        text='invercity',
                                        variable=self.is_inversion,
                                        command=self.update_img)
        
        self.is_binarisation        = StringVar(value='0')
        self.binarisation_switch    = MySwitch(self.functions_frame,
                                        text='binarisation',
                                        variable=self.is_binarisation,
                                        command=self.update_img)
        self.binarisation_var_label = CTkLabel(self.functions_frame, text='100')
        self.binarisation_var       = tk.IntVar()
        self.binarisation_var.set(100)
        self.slider                 = CTkSlider(self.functions_frame, from_=0, to=255, number_of_steps=255, width=300,
                                        variable=self.binarisation_var, command=self.upadate_binarisation_var)
        
        self.figure = plt.Figure(figsize=(3, 1), dpi=100)

        self.ax = self.figure.add_subplot(111)
        self.ax.set_axis_off()
        
        histogram = cv2.calcHist([cv2.cvtColor(self.preview_frame, cv2.COLOR_BGR2GRAY)], [0], None, [256], [0, 256])
        x = np.linspace(0, 255, 256)
        self.graph, = self.ax.plot(x, histogram)
        self.line = self.ax.axvline(x=100)
        
        self.hist_canvas = FigureCanvasTkAgg(self.figure, self.functions_frame)        
        
        self.preview = Output_display(self.master, self.preview_frame, self.conversion)
        self.draw_widgets()
        
    def upadate_binarisation_var(self, var):
        self.line.set_xdata([var])
        self.binarisation_var_label.configure(text=f'{int(var)}')
        self.update_img()
        
    
    def conversion(self, img):
        if self.is_binarisation.get() == '1':
            mask = img <= int(self.binarisation_var.get())
            img[mask] = 0
            img[~mask] = 255
        
        if self.is_inversion.get() == '1':
            img = 255 - img
        
        return img
            
    def update_img(self):
        histogram = cv2.calcHist([cv2.cvtColor(self.preview_frame, cv2.COLOR_BGR2GRAY)], [0], None, [256], [0, 256])
        self.graph.set_ydata(histogram)
        self.hist_canvas.draw()
        
        
        self.preview.is_gray = True
        self.preview.on_change()


    def draw_widgets(self):
        
        self.functions_frame.pack()
        
        self.inversion_switch.grid(             row=0, column=0, sticky=W, padx=10, pady=5)
        
        self.binarisation_switch.grid(          row=1, column=0, sticky=W, padx=10, pady=5)
        self.slider.grid(                       row=3, column=1, sticky=W, padx=10, pady=5)
        self.binarisation_var_label.grid(       row=4, column=1, sticky=N, padx=10, pady=5)
        
        self.hist_canvas.get_tk_widget().grid(  row=2, column=1, padx=10, pady=5)
        
        
        self.update_img()
        self.preview.pack()
        