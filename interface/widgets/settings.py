from  customtkinter import *
import tkinter as tk

from settings.rgb_bw import Settings
class SettingsBlock:
    def __init__(self, master, name, min, max, command=None):
        self.root = master
        self.name  = name
     
        def new_command(*args, **kwargs):
            self.lable_var.configure(text=self.get_current_value())
            if command is not None:
                return command(*args, **kwargs)
        
        self.var = tk.DoubleVar()
        self.slider = CTkSlider(self.root, from_=min, to=max, variable=self.var, command=new_command)

        
        self.lable_name = CTkLabel(self.root, text=self.name)
        self.lable_var = CTkLabel(self.root, text=self.get_current_value())
        

    
    def get_current_value(self):
        return '{: .2f}'.format(self.var.get())
    
    def pack(self):
        self.lable_name.pack(pady=5)
        self.slider.pack(pady=5)
        self.lable_var.pack(pady=5)
        
        
        
class SettingsMenu:
    def __init__(self, master = None, commands=None) -> None:
        if master is None:
            master = CTk()    
        self.root = master
        if commands is None:
            commands = [None] * 5
        self.__intensity_block = SettingsBlock(self.root, 'Интенсивность', -127, 127, commands[0])
        self.__brightness_block = SettingsBlock(self.root, 'Яркость', -127, 127, commands[1])
        self.__red_block = SettingsBlock(self.root, 'Красный', -127, 127, commands[2])
        self.__green_block = SettingsBlock(self.root, 'Зеленый', -127, 127, commands[3])
        self.__blue_block = SettingsBlock(self.root, 'Синий', -127, 127, commands[4])
    
    @property
    def intensity(self):
        return self.__intensity_block.var.get()
    
    @property
    def brightness(self):
        return self.__brightness_block.var.get()
    
    @property
    def red(self):
        return self.__red_block.var.get()
    
    @property
    def green(self):
        return self.__green_block.var.get()
    
    @property
    def blue(self):
        return self.__blue_block.var.get()
    
        
    def pack(self):
        self.__intensity_block.pack()
        self.__brightness_block.pack()
        self.__red_block.pack()
        self.__green_block.pack()
        self.__blue_block.pack()
        