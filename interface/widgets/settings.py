from  customtkinter import *
import tkinter as tk

class Settings_block:
    def __init__(self, place, name):
        self.palce = place
        self.name  = name

    def draw_slider(self, min, max, command=None):
        lbl = CTkLabel(self.palce, text=self.name)
        lbl.pack(pady=5)
        self.var = tk.DoubleVar()
        self.sldr = CTkSlider(self.palce, from_=min, to=max, variable=self.var, command=command)
        self.sldr.pack(pady=5)
        self.num = CTkLabel(self.palce, text=self.get_current_value())
        self.num.pack(pady=5)
    
    def get_current_value(self):
        return '{: .2f}'.format(self.var.get())
    
    def slider_changed(self):
        self.num.configure(text=self.get_current_value())