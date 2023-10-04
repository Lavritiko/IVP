from  customtkinter import *
import pyautogui
from interface.cap_pic import PicWindow
from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np


class CapturePic:
    def __init__(self, parent):
        self.root = CTkToplevel(parent)
        self.root.withdraw()
        self.root.attributes("-transparent", "maroon3")
        self.start_x = None
        self.start_y = None
        self.current_x = None
        self.current_y = None
        self.picture_frame = CTkFrame(self.root, fg_color=None)
        self.picture_frame.pack(expand=True, fill=BOTH)       

    def create_screen_canvas(self):
        self.root.deiconify()
        # CTk().withdraw()

        self.canvas = CTkCanvas(self.picture_frame, cursor="cross", bg="grey1")
        self.canvas.pack(expand=YES, fill=BOTH)

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_snip_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.canvas.bind("<Button-2>", self.on_drag_start)
        self.canvas.bind("<B2-Motion>", self.on_drag_motion)
        self.canvas.bind("<ButtonRelease-2>", self.on_drag_end)
        
        self.canvas.bind("<Button-3>", self.on_drag_start)
        self.canvas.bind("<B3-Motion>", self.on_resize_motion)
        self.canvas.bind("<ButtonRelease-3>", self.on_resize_end)

        self.root.bind("<Return>", self.hide_cord)
        self.root.bind("<Escape>", self.close_capute)
        self.root.bind("<KeyRelease-Return>", self.cap_pic)

        self.root.attributes('-fullscreen', True)
        self.root.attributes('-alpha', .3)
        self.root.lift()
        self.root.attributes('-topmost', True)

        self.cord = CTkLabel(self.picture_frame, bg_color='grey10')       

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.canvas.create_rectangle(0, 0, 1, 1, fill="maroon3")

    def on_snip_drag(self, event):
        self.cord.place_forget()
        self.current_x, self.current_y = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.canvas.coords(1, self.start_x, self.start_y, self.current_x, self.current_y)

    def on_button_release(self, event):
        self.display_rectangle_position()
        
        return event
    
    def display_rectangle_position(self):
        
        self.cord.place(x=self.start_x, y=self.start_y)
        self.cord.configure(text=f"(x1: {self.start_x}, y1: {self.start_y}), (x2: {self.current_x}, y2: {self.current_y})")

        print(self.start_x)
        print(self.start_y)
        print(self.current_x)
        print(self.current_y)

    def on_drag_start(self, event):
        self.drag_start_x = event.x
        self.drag_start_y = event.y
    
    def on_drag_motion(self, event):
        self.x = self.start_x - event.x + self.drag_start_x
        self.y = self.start_y - event.y + self.drag_start_y
        self.x2 = self.current_x - event.x + self.drag_start_x
        self.y2 = self.current_y - event.y + self.drag_start_y
        self.canvas.coords(1, self.x, self.y, self.x2, self.y2)
        self.cord.place(x=self.x, y=self.y)
        self.cord.configure(text=f"(x1: {self.x}, y1: {self.y}), (x2: {self.x2}, y2: {self.y2})")

    def on_resize_motion(self, event):
        self.x = self.start_x - event.x + self.drag_start_x
        self.y = self.start_y - event.y + self.drag_start_y
        self.canvas.coords(1, self.x, self.y, self.current_x, self.current_y)
        self.cord.place(x=self.x, y=self.y)
        self.cord.configure(text=f"(x1: {self.x}, y1: {self.y}), (x2: {self.current_x}, y2: {self.current_y})")

    def on_drag_end(self, event):
        self.start_x = self.x
        self.start_y = self.y
        self.current_x = self.x2
        self.current_y = self.y2
    
    def on_resize_end(self, event):
        self.start_x = self.x
        self.start_y = self.y

    def take_bounded_screenshot(self, x1, y1, x2, y2):
        image = pyautogui.screenshot(region=(x1, y1, x2, y2))
        title_name = f"Экран ({self.start_x}, {self.start_y}) - ({self.current_x}, {self.current_y})"
        image_cv = np.array(image)
        image2 = ImageTk.PhotoImage(image)
        PicWindow(self.root, 1024, 768, image2, image_cv=image_cv, title=title_name)

    def hide_cord(self, event):
        self.cord.place_forget()

    def cap_pic(self, event):
        
        if self.start_x <= self.current_x and self.start_y <= self.current_y:
            print("right down")
            self.take_bounded_screenshot(self.start_x, self.start_y, self.current_x - self.start_x, self.current_y - self.start_y)

        elif self.start_x >= self.current_x and self.start_y <= self.current_y:
            print("left down")
            self.take_bounded_screenshot(self.current_x, self.start_y, self.start_x - self.current_x, self.current_y - self.start_y)

        elif self.start_x <= self.current_x and self.start_y >= self.current_y:
            print("right up")
            self.take_bounded_screenshot(self.start_x, self.current_y, self.current_x - self.start_x, self.start_y - self.current_y)

        elif self.start_x >= self.current_x and self.start_y >= self.current_y:
            print("left up")
            self.take_bounded_screenshot(self.current_x, self.current_y, self.start_x - self.current_x, self.start_y - self.current_y)
        
        self.picture_frame.destroy()
        self.root.withdraw()
        # CTk().deiconify()
    
    def close_capute(self, event):
        self.root.destroy()

