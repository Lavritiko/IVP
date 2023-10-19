import cv2 as cv
import customtkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

if __name__ == '__main__':
    from widgets.video_screan import VideoScreen
else:
    from interface.widgets.video_screan import VideoScreen

class VideoPlayer():
    def __init__(self, master, video_capture, title='Child', resizable=(False, False)):
        self.master = master
        self.video_capture = video_capture
        
        # h_video = self.video_capture.get(cv.CAP_PROP_FRAME_HEIGHT)
        # w_video = self.video_capture.get(cv.CAP_PROP_FRAME_WIDTH)
        
        self.root = tk.CTkToplevel(master)
        self.root.title(title)
        self.root.configure(background='gray22')
        self.root.resizable(resizable[0], resizable[1])
        
        # ========================== Create wigets ==========================
        
        self.tab_view = tk.CTkTabview(self.root)
        self.tab_view.add('Видео')
        self.tab_view.add('Настройки')
        
        self.video_screan = VideoScreen(self.tab_view.tab('Видео'), video_capture)
        
        self.switch_var = tk.StringVar(value='off')
        self.switch = tk.CTkSwitch(self.tab_view.tab('Видео'),
                                text='Switch',
                                command=self.switch_callback, 
                                variable=self.switch_var, 
                                width=150, height=30, 
                                onvalue='on', offvalue='off')
        
        self.slider = tk.CTkSlider(self.root, from_=0, to=100)
        
        
        self.draw_widjets()
        
        
    def draw_widjets(self):
        self.root.grab_set()
        
        self.tab_view.pack()
        self.switch.pack()
        self.slider.pack()


        
    def start(self):
        self.root.mainloop()
        
    def switch_callback(self):
        if self.switch_var.get() == 'on':
            pass
        else:
            pass
          
if __name__ == '__main__':
    # window = tk.CTk()
    
    path = filedialog.askopenfilename()
    video_capture = cv.VideoCapture(path)
    
    a = VideoPlayer(None, video_capture)
    
    # window.mainloop()
    a.start()
