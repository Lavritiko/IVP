import cv2 as cv
from  customtkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from interface.widgets.switch_widget import Switch
from interface.widgets.video_screen import VideoScreen
from interface.widgets.settings import Settings_block
from settings.rgb_bw import Settings

class VideoPlayer():
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
        self.hmm = Settings(self.video_capture)
        self.switch_var = StringVar(value='off')
        self.rgb_gray_switch = Switch(self.tab_view.tab('Видео'), 'RGB-Gray')

        self.bt = CTkButton(self.tab_view.tab('Видео'), text='stop', command=self.video_screan.stop_start)
        self.sl = CTkSlider(self.tab_view.tab('Видео'), from_=0.2, to=3, command=self.video_screan.set_delay)
        
        # self.slider = CTkSlider(self.root, from_=0, to=100)
        
        
        self.draw_widjets()
        self.draw_widgets_settings(self.tab_view.tab("Настройки"))
        
        
    def draw_widjets(self):
        self.root.grab_set() 
        self.tab_view.pack()
        self.rgb_gray_switch.draw_switch(self.switch_var, self.switch_callback)
        self.video_screan.pack()
        self.bt.pack()
        self.sl.pack()

    def draw_widgets_settings(self, tab_settings):

        Settings_block(tab_settings, 'Интенсивность').draw_slider(-127, 127, command=self.hmm.contrast)
        Settings_block(tab_settings, 'Яркость').draw_slider(-127, 127, command=self.hmm.brightness)
        Settings_block(tab_settings, 'Красный').draw_slider(-127, 127, command=self.hmm.red)
        Settings_block(tab_settings, 'Зеленый').draw_slider(-127, 127, command=self.hmm.green)
        Settings_block(tab_settings, 'Синий').draw_slider(-127, 127, command=self.hmm.blue)
        
    def start(self):
        self.root.mainloop()
        
    def switch_callback(self):
        # if self.switch_var.get() == 'on':
        #     vid = self.hmm.gray()
        #     print(vid)
        #     self.video_screan.on_change(vid)

        # else:
        #     self.video_screan.on_change(self.video_capture)
        
        if self.switch_var.get() == 'on':
            pass
        else:
            pass
          
# if __name__ == '__main__':
#     # window = tk.CTk()
    
#     path = filedialog.askopenfilename()
#     video_capture = cv.VideoCapture(path)
    
#     a = VideoPlayer(None, video_capture)
    
#     # window.mainloop()
#     a.start()
