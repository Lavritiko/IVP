from  customtkinter import *
from interface.message_box import MessageBox
from interface.cap_pic import PicWindow
from interface.capture_p import CapturePic
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2

class Menu_win:
    def __init__(self, resizable=(False, False)):
        set_appearance_mode("dark")
        set_default_color_theme('dark-blue')
        self.root = CTk()
        self.root.title("IPV")
        self.root.resizable(resizable[0], resizable[1])

    def start(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        hmm = StringVar(value="Input")
        btn1 = CTkOptionMenu(self.root, values=["Select Picture", "Capture Picture", "Select Video", "Capture Video"], variable=hmm, command=self.input_callback)
        about = CTkButton(self.root, text="about", command=self.about)
        btn1.pack(side="left")
        about.pack(side="left")

    def input_callback(self, choice):
        if choice == "Select Picture":
            self.select_image()
        elif choice == "Capture Picture":
            CapturePic(self.root).create_screen_canvas()

    def select_image(self):
        path = filedialog.askopenfilename()
        if len(path) > 0:
            image = cv2.imread(path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image2 = Image.fromarray(image)
            image2 = ImageTk.PhotoImage(image2)
            PicWindow(self.root, 1024, 768, image2, image_cv=image)
    
    def about(self):
        info = "Created by: \n me XD \n  2023"
        MessageBox(self.root, title="About", message=info, high=200, width=270)
