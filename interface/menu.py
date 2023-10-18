from  customtkinter import *
from interface.widgets.message_box import MessageBox
from interface.cap_pic import PicWindow
from interface.capture_p import CapturePic
from tkinter import filedialog
import cv2

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
        
        vid_capture = cv2.VideoCapture(path)
        if (not vid_capture.isOpened()):
            raise Exception("Error opening the video file")
        
        fps = vid_capture.get(cv2.CAP_PROP_FPS)

        print('Frames per second : ', fps,'FPS')
        frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
        print('Frame count : ', frame_count)
        
        _, image = vid_capture.read()
        PicWindow(self.root, 1024, 768, image_cv=image)
        
        
        while(vid_capture.isOpened()):
            ret, frame = vid_capture.read()
            if ret == True: 
                cv2.imshow('Frame',frame)
                key = cv2.waitKey(20)
                
                if key == ord('q'):
                    break
            else:
                print('end')
                break
        
        vid_capture.release()
        cv2.destroyAllWindows()
        
    def captureVideo(self):
        print('captureVideo')
        raise Exception('functionality in development')
        
    
    def start(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        hmm = StringVar(value="Input")
        btn1 = CTkOptionMenu(self.root, values=[*self.possible_functionality.keys()], variable=hmm, command=self.input_callback)
        about = CTkButton(self.root, text="about", command=self.about)
        btn1.pack(side="left")
        about.pack(side="left")

    
    def input_callback(self, choice):
        self.possible_functionality[choice]()
    
    def about(self):
        info = "Created by: \n Lavrentsova Anna, Feklin Nikita XD \n  2023"
        MessageBox(self.root, title="About", message=info, high=200, width=270)
