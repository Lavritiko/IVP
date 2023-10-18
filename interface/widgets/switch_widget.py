from  customtkinter import *

class Switch:
    def __init__(self, place, text):
        self.place = place
        self.text = text
    
    def draw_switch(self, var, command):
        
        sw = CTkSwitch(self.place, text=self.text, command=command, variable=var, width=150, height=30, onvalue='on', offvalue='off')
        sw.pack()