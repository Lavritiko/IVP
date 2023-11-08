from  customtkinter import *
import pyautogui
from interface.picture_window import PicWindow
import cv2
import numpy as np

class CapturePic:
    def __init__(self, parent):
        self.root = CTkToplevel(parent)
        self.root.withdraw()
        self.root.attributes('-transparent', "maroon3")
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', .2)
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.deiconify()

        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None

        self.picture_frame = CTkFrame(self.root, fg_color=None)
        self.picture_frame.pack(expand=True, fill=BOTH)              

    def create_screen_canvas(self):

        self.canvas = CTkCanvas(self.picture_frame, cursor="cross", bg="grey1")
        self.canvas.pack(expand=YES, fill=BOTH)

        # ========================== Create canvas ==========================

        self.canvas.bind("<ButtonPress-1>", self.on_button_press) 
        self.canvas.bind("<B1-Motion>", self.on_snip_drag) 
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release) 

        # ========================== Drag canvas ==========================

        self.canvas.bind("<Button-2>", self.on_change_start)
        self.canvas.bind("<B2-Motion>", self.on_drag_motion)
        self.canvas.bind("<ButtonRelease-2>", self.on_change_end)
        
        # ========================== Resize canvas ==========================

        self.canvas.bind("<Button-3>", self.on_change_start)
        self.canvas.bind("<B3-Motion>", self.on_resize_motion)
        self.canvas.bind("<ButtonRelease-3>", self.on_change_end)

        # ========================== Take Screenshot ==========================

        self.root.bind("<Return>", func=None) # Зажать клавишу Энтер
        self.root.bind("<KeyRelease-Return>", self.take_screenshot)

        # ========================== Cancel capture mode ==========================

        self.root.bind("<Escape>", self.close_capture)  

        self.coordinates = CTkLabel(self.picture_frame, bg_color='white', text_color='black')   

    def display_rectangle_position(self):
        x_min = min(self.start_x, self.current_x)
        y_min = min(self.start_y, self.current_y)
        self.coordinates.place(x = x_min, y = y_min - 28) #palce coordinates top left

        self.coordinates.configure(text=f"(x1: {self.start_x}, y1: {self.start_y}), (x2: {self.current_x}, y2: {self.current_y})")

        print(self.start_x)
        print(self.start_y)
        print(self.current_x)
        print(self.current_y)

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.canvas.create_rectangle(0, 0, 1, 1, fill="maroon3")

    def on_snip_drag(self, event):
        self.coordinates.place_forget()
        self.current_x, self.current_y = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.canvas.coords(1, self.start_x, self.start_y, self.current_x, self.current_y)

    def on_button_release(self, event):
        self.display_rectangle_position()

    def on_change_start(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y
    
    def on_drag_motion(self, event):
        self.x = self.start_x + event.x - self.drag_start_x
        self.y = self.start_y + event.y - self.drag_start_y
        self.x2 = self.current_x + event.x - self.drag_start_x
        self.y2 = self.current_y + event.y - self.drag_start_y

        self.canvas.coords(1, self.x, self.y, self.x2, self.y2)
        self.coordinates.configure(text=f"(x1: {self.x}, y1: {self.y}), (x2: {self.x2}, y2: {self.y2})")

    def on_resize_motion(self, event):
        self.x = self.start_x
        self.y = self.start_y
        self.x2 = self.current_x + event.x - self.drag_start_x
        self.y2 = self.current_y + event.y - self.drag_start_y

        self.canvas.coords(1, self.start_x, self.start_y, self.x2, self.y2)
        self.coordinates.configure(text=f"(x1: {self.start_x}, y1: {self.start_y}), (x2: {self.x2}, y2: {self.y2})")

    def on_change_end(self, event):
        self.start_x = self.x
        self.start_y = self.y
        self.current_x = self.x2
        self.current_y = self.y2

        self.display_rectangle_position()
        
    def take_screenshot(self, event):
        x1 = min(self.start_x, self.current_x)
        y1 = min(self.start_y, self.current_y)

        x2 = max(self.start_x, self.current_x)
        y2 = max(self.start_y, self.current_y)

        image = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
        title_name = f"Экран ({self.start_x}, {self.start_y}) - ({self.current_x}, {self.current_y})"
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        PicWindow(self.root, 1024, 768, image_cv, title=title_name)
        
        self.picture_frame.destroy()
        self.root.withdraw()
    
    def close_capture(self, event):
        self.root.destroy()

