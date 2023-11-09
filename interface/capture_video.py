from interface.capture_picture import CapturePic
from  customtkinter import *
import pyautogui
from interface.picture_window import PicWindow
from interface.video_player import VideoPlayerWindow
import cv2
import numpy as np


class CaptureVideo(CapturePic):
    def __init__(self, parent):
        super().__init__(parent)
        self.state = 0
        
        
    def take_screenshot(self, event):
        self.state += 1
        if self.state == 1:
            self.x_0 = int(min(self.start_x, self.current_x))
            self.y_0 = int(min(self.start_y, self.current_y))

            self.x_size = int(abs(self.start_x - self.current_x))
            self.y_size = int(abs(self.start_y - self.current_y))
            self.fps = 20.0
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.out = cv2.VideoWriter('output.avi', fourcc, self.fps, (self.x_size, self.y_size))
            self.video_recording()
            


            
        # title_name = f"Экран ({self.start_x}, {self.start_y}) - ({self.current_x}, {self.current_y})"

        
        
    def video_recording(self):
        print(self.state)
        img = pyautogui.screenshot(region=(self.x_0, self.y_0, self.x_size, self.y_size))
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.out.write(frame)
        if self.state == 1:
            self.root.after(int(1000 / self.fps), self.video_recording)
        elif self.state > 1:
            self.out.release()
            vid_capture = cv2.VideoCapture('output.avi')
            VideoPlayerWindow(self.root, vid_capture)
            self.picture_frame.destroy()
            self.root.withdraw()
