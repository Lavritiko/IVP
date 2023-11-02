from  customtkinter import *
from interface.widgets.message_box import MessageBox
from interface.cap_pic import PicWindow
from interface.capture_p import CapturePic
from interface.video_player import  VideoPlayerWindow
from tkinter import filedialog
import cv2

import pyautogui
import numpy as np
from interface.video_player import VideoPlayerWindow

class Menu_win:
    def __init__(self, resizable=(False, False)):
        set_appearance_mode("dark")
        set_default_color_theme('dark-blue')
        self.root = CTk()
        self.root.title("IPV")
        self.root.resizable(resizable[0], resizable[1])
        
        self.possible_functionality: dict = {
            'Select Picture':   self.selectPicture,
            'Capture Picture':  self.capturePicture,
            'Select Video':     self.selectVideo,
            'Capture Video':    self.captureVideo
        }        
        '''
        to add functionality, just add a couple:
            key: the text of the menu element and 
            value: the function to be called
        '''
        
        self.hmm = StringVar(value="Input")
        self.btn1 = CTkOptionMenu(self.root, values=[*self.possible_functionality.keys()], variable=self.hmm, command=self.input_callback)
        self.about = CTkButton(self.root, text="about", command=self.about)
    
    def selectPicture(self):
        path = filedialog.askopenfilename()
        if len(path) > 0:
            image = cv2.imread(path)
            PicWindow(self.root, 1024, 768, image_cv=image)
        
    def capturePicture(self):
        CapturePic(self.root).create_screen_canvas()
        
    def selectVideo(self):
        print('selectVideo')
        path = filedialog.askopenfilename()
        if len(path) > 0:
            vid_capture = cv2.VideoCapture(path)
            VideoPlayerWindow(self.root, vid_capture)
        
    def captureVideo(self):
        print('captureVideo')
        SCREEN_SIZE = (1920, 1080)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (SCREEN_SIZE))
        while True:
            img = pyautogui.screenshot(region=(0,0, 1920, 1080))
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            cv2.imshow('screanshot', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cv2.destroyAllWindows()
        out.release()
        vid_capture = cv2.VideoCapture('output.avi')
        VideoPlayerWindow(self.root, vid_capture)
        # raise Exception('functionality in development')
        
    
    def start(self):
        self.pack()
        self.root.mainloop()

    def pack(self):
        self.btn1.pack(side="left")
        self.about.pack(side="left")
    
    def input_callback(self, choice):
        self.possible_functionality[choice]()
    
    def about(self):
        info = "Created by: \n Lavrentsova Anna, Feklin Nikita XD \n  2023"
        MessageBox(self.root, title="About", message=info, high=200, width=270)
