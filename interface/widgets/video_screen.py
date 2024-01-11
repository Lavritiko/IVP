import cv2 as cv
import customtkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from settings.rgb_bw import gray, IS_UPDATE_FUCKING_STATISTICS

class VideoScreen():
    def __init__(self, master, video_capture) -> None:
        self.video_capture = video_capture
        self.master = master
        
        h = self.video_capture.get(cv.CAP_PROP_FRAME_HEIGHT)
        w = self.video_capture.get(cv.CAP_PROP_FRAME_WIDTH)
        
        self.norm_fps = self.video_capture.get(cv.CAP_PROP_FPS)
        self.fps = self.norm_fps
        self.root = tk.CTkCanvas(self.master, height=h, width=w)
        self.root.configure(background='gray22')
        
        self.labdel_fps = tk.CTkLabel(master, text=str(self.fps))
        self.play = True
        self.is_gray = False
        self.br, self.cnt, self.r, self.g, self.b = 0, 0, 0, 0, 0
        
        ret, self.frame = self.video_capture.read()
        self.update()
    

    def set_delay(self, fps: int):
        self.fps = fps
        self.labdel_fps.configure(text=str(fps))
        print(fps)
    
    
    def update(self):
        global IS_UPDATE_FUCKING_STATISTICS
        if self.play:
            ret, self.frame = self.video_capture.read()

            if ret:
                if self.is_gray:
                    self.frame = gray(self.frame, self.br, self.cnt, self.r, self.g, self.b)
                self.frame = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)

                self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.frame))
                IS_UPDATE_FUCKING_STATISTICS[0] = True
                self.root.create_image(0, 0, image=self.photo, anchor=tk.NW)
            else:
                self.video_capture.set(cv.CAP_PROP_POS_MSEC, 0)

        self.master.after(int(1000 / self.fps), self.update)
        
    def stop_start(self):
        self.play = not self.play
        
    def pack(self):
        self.root.pack()
        self.labdel_fps.pack()

        
          
if __name__ == '__main__':
    window = tk.CTk()
    
    path = filedialog.askopenfilename()
    video_capture = cv.VideoCapture(path)
    window.configure(background='gray22')
    video = VideoScreen(window, video_capture)
    
    bt = tk.CTkButton(window, text='stop', command=video.stop_start)
    sl = tk.CTkSlider(window, from_=1, to=100, number_of_steps=99, command=video.set_delay)

    
    video.pack()
    bt.pack(pady=10)
    sl.pack(pady=10)
    
    window.mainloop()
    