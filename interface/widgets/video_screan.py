import cv2 as cv
import customtkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog


class VideoScreen():
    def __init__(self, master, video_capture) -> None:
        self.video_capture = video_capture
        self.master = master
        
        h = self.video_capture.get(cv.CAP_PROP_FRAME_HEIGHT)
        w = self.video_capture.get(cv.CAP_PROP_FRAME_WIDTH)
        self.norm_fps = int(1000 / self.video_capture.get(cv.CAP_PROP_FPS))
        self.delay = self.norm_fps
        
        self.root = tk.CTkCanvas(master, height=h, width=w)
        self.root.configure(background='gray22')
        
                
        self.play = True
        self.update()
    

    def set_delay(self, koef):
        self.delay = int(self.norm_fps / koef)
    
    
    def update(self):
        if self.play:
            ret, frame = self.video_capture.read()
        
            if ret:
                frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.root.create_image(0, 0, image=self.photo, anchor=tk.NW)
            else:
                self.video_capture.set(cv.CAP_PROP_POS_MSEC, 0)

        self.master.after(self.delay, self.update)
        
    def stop_start(self):
        self.play = not self.play
        

        
    def pack(self):
        self.root.pack()
            
        
          
if __name__ == '__main__':
    window = tk.CTk()
    
    path = filedialog.askopenfilename()
    video_capture = cv.VideoCapture(path)
    window.configure(background='gray22')
    video = VideoScreen(window, video_capture)
    
    bt = tk.CTkButton(window, text='stop', command=video.stop_start)
    sl = tk.CTkSlider(window, from_=0.2, to=3, command=video.set_delay)
    
    video.pack()
    bt.pack(pady=10)
    sl.pack(pady=10)
    # window.mainloop()
    
    window.mainloop()
    
