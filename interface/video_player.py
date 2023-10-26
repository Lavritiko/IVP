import cv2 as cv
from  customtkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from interface.widgets.switch_widget import Switch
from interface.widgets.video_screen import VideoScreen
from interface.widgets.settings import SettingsMenu
from settings.rgb_bw import Settings
import tkinter as tk
class VideoPlayerWindow():
    def __init__(self, master, video_capture, title='Child', resizable=(False, False)):
        self.master = master
        self.video_capture = video_capture
        
        # h_video = self.video_capture.get(cv.CAP_PROP_FRAME_HEIGHT)
        # w_video = self.video_capture.get(cv.CAP_PROP_FRAME_WIDTH)
        
        self.root = CTkToplevel(master)
        self.root.title(title)
        self.root.configure(background='gray22')
        self.root.resizable(resizable[0], resizable[1])
        
        # ========================== Create wigets ==========================
        
        self.tab_view = CTkTabview(self.root)
        self.tab_view.add('Видео')
        self.tab_view.add('Настройки')
        
        self.video_screan = VideoScreen(self.tab_view.tab('Видео'), video_capture)
        
        # self.hmm = Settings(self.video_capture)
        
        self.switch_var = StringVar(value='off')
        self.rgb_gray_switch = Switch(self.tab_view.tab('Видео'), 'RGB-Gray')

        
        self.bt = CTkButton(self.tab_view.tab('Видео'), text='stop', command=self.pressing_button_stop_start)
        self.fps = tk.IntVar()
        self.sl = CTkSlider(self.tab_view.tab('Видео'), 
                            from_=1, to=100, number_of_steps=99,  
                            variable=self.fps, 
                            command=self.video_screan.set_delay)
        
        # self.slider = CTkSlider(self.root, from_=0, to=100)
        self.settings = SettingsMenu(self.tab_view.tab("Настройки"))
        
        self.draw_widjets()
        

        
    def pressing_button_stop_start(self, *args, **kwargs): 
        if self.bt._text == 'stop':
            self.bt.configure(text='start')
        else:
            self.bt.configure(text='stop')
        return self.video_screan.stop_start(*args, **kwargs)
    
    def draw_widjets(self):
        self.root.grab_set() 
        self.tab_view.pack()
        
        # =============== Видео ========================
        self.rgb_gray_switch.draw_switch(self.switch_var, self.switch_callback)
        self.video_screan.pack()
        self.bt.pack()
        self.sl.pack()
        
        # =============== Настройки ==================
        # self.settings.pack()

        
    def switch_callback(self):    
        if self.switch_var.get() == 'on':
            pass
        else:
            pass
          
if __name__ == '__main__':
    
    path = filedialog.askopenfilename()
    video_capture = cv.VideoCapture(path)
    
    a = VideoPlayerWindow(None, video_capture)
    a.root.mainloop()
