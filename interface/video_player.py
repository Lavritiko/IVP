import cv2 as cv
from  customtkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from interface.widgets.switch_widget import MySwitch
from interface.widgets.video_screen import VideoScreen
from interface.widgets.settings import SettingsMenu
from settings.rgb_bw import gray
import tkinter as tk
from .statistics_window import StatisticsWindow


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
        
        self.tab_view = CTkTabview(self.root, command=self.select_menu)
        self.tab_view.add('Видео')
        self.tab_view.add('Настройки')
        
        self.video_screan = VideoScreen(self.tab_view.tab('Видео'), video_capture)
        
        self.switch_is_gray_var = StringVar(value='1')
        
        self.rgb_gray_switch = MySwitch(self.tab_view.tab('Видео'),
                                        text='RGB-Gray',
                                        variable=self.switch_is_gray_var,
                                        command=self.switch_callback)

        self.statistics_button = CTkButton(self.tab_view.tab('Видео'), text='Статистика', command=self.statistics_button_callback)
        self.bt = CTkButton(self.tab_view.tab('Видео'), text='stop', command=self.pressing_button_stop_start)
        self.fps = tk.IntVar()
        self.sl = CTkSlider(self.tab_view.tab('Видео'), 
                            from_=1, to=100, number_of_steps=99,  
                            variable=self.fps,
                            command=self.video_screan.set_delay,
                            )
        self.sl.set(self.video_screan.fps)
        
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
        self.rgb_gray_switch.pack()
        self.video_screan.pack()
        self.bt.pack()
        self.sl.pack()
        
        # =============== Настройки ==================
        self.settings.pack()

    def select_menu(self):
        if self.switch_is_gray_var.get() == '1':
            self.rgb_gray_switch.toggle()
        
        
    def switch_callback(self):
        if self.switch_is_gray_var.get() == '1':
            self.video_screan.is_gray = True
            self.video_screan.br = self.settings.brightness
            self.video_screan.cnt = self.settings.intensity
            self.video_screan.r = self.settings.red
            self.video_screan.g = self.settings.green
            self.video_screan.b = self.settings.blue
        else:
            self.video_screan.is_gray = False

    def statistics_button_callback(self):
        pass

          
if __name__ == '__main__':
    
    path = filedialog.askopenfilename()
    video_capture = cv.VideoCapture(path)
    
    a = VideoPlayerWindow(None, video_capture)
    a.root.mainloop()