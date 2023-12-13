from  customtkinter import *
import cv2
from PIL import Image
from PIL import ImageTk
import numpy as np
from interface.widgets.additional_paramas import AdditionalParamasFrame
from interface.picture_window import PicWindow
from interface.widgets.preview_screen import PreviewScreen
from interface.video_player import VideoPlayerWindow

class ModelCreatingWindow():
    def __init__(self, parent, title):
        self.root = CTkToplevel(parent)
        self.root.geometry("1030x700")
        self.root.resizable(False, False)
        self.root.title(title)
        self.root.grab_set()
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        self.modeling_frame         = CTkFrame(self.root, corner_radius=0)
        self.modeling_frame_label   = CTkLabel(self.modeling_frame, text="Моделирование",
                                            compound='left', font=CTkFont(size=15, weight='bold'))
        self.model_type             = None


        # ########## create Size model widget #################
        self.size_input_frame       = CTkFrame(self.modeling_frame_label, corner_radius=5, fg_color=("gray10", "gray10"))
        self.size_input_label       = CTkLabel(self.size_input_frame, text="Введите размер модели")
        self.size_input_x           = CTkEntry(self.size_input_frame, placeholder_text='X', width=50)
        self.size_input_x.insert(0, '450')
        self.size_input_y           = CTkEntry(self.size_input_frame, placeholder_text='Y', width=50)
        self.size_input_y.insert(0, '450')
        


        # ######### create model selection widget ##############
        self.model_input_frame      = CTkFrame(self.modeling_frame_label, corner_radius=5, fg_color=("gray10", "gray10"))
        self.model_input_label      = CTkLabel(self.model_input_frame, text="Выберите модель")
        
        self.model_possible_functionality: dict = {
             'Задержанный единичный импульс': self.delayed_single_impulse,
             'Задержанный единичный скачок': self.delayed_single_hop,
             'Одиночный круг': self.single_circle,
             'Одиночный квадрат': self.single_square,
             'Шахматная доска': self.chessboard,
             'Круги в узлах прямоугольной решетки': self.circles_at_nodes,
             'Случайные круги': self.random_circles,
             'Белый шум с равномерным распределением': self.noise_uniform_distribution,
             'Белый шум с нормальным распределением': self.noise_normal_distribution,
             'Плоская гравитационная волна': self.flat_gravitational_wave,
        }
        
        def model_input_callback(choice):
            self.model_type = choice
            self.model_possible_functionality[choice]()
                
        self.model_var              = StringVar(value="Choose a model")
        self.model_option           = CTkOptionMenu(self.model_input_frame, values=[*self.model_possible_functionality.keys()], variable=self.model_var, command=model_input_callback, width=325)


        # ######### create selection of parameters widget ############
        self.additional_input_label = CTkLabel(self.modeling_frame_label, text="Дополнительные параметры", font=CTkFont(size=13, weight='bold'))
        self.additional_input_frame = AdditionalParamasFrame(self.modeling_frame_label)
        

        ########### create preview widget ###########################
        self.model_button           = CTkButton(self.modeling_frame, text="Смоделировать", command=self.model_button_callback)
        
        self.preview_frame          = CTkFrame(self.root, corner_radius=0, fg_color="transparent")
        self.previw_label           = CTkLabel(self.preview_frame, text="Предварительный просмотр",
                                                font=CTkFont(size=15, weight='bold'))
        self.preview_canvas         = PreviewScreen(self.preview_frame)

        self.accept_button          = CTkButton(self.preview_frame, text="Принять", command=self.accept_button_callback)
        

        ###########################################################
        self.draw_widgets()
        

    def draw_widgets(self):
        
        ################ 1 блок. Настройка моделирования ############################
        self.modeling_frame.grid(       row=0, column=0, sticky=NSEW)
        self.modeling_frame.grid_rowconfigure(6, weight=1)
        self.modeling_frame_label.grid( row=0, column=0, pady=10)
        
        
        ################# 1.1 блок. Размер изображения #############################
        self.size_input_frame.grid( row=1, column=0, sticky=NSEW, padx=10, pady=10, ipady=5)
        self.size_input_frame.grid_columnconfigure(0, minsize=200)
        self.size_input_label.grid( row=0, column=0, sticky=W, padx=10, pady=10)
        self.size_input_x.grid(     row=1, column=0, sticky=W, padx=10)
        self.size_input_y.grid(     row=1, column=0, padx=10)
        
        
        ################ 1.2 блок. Вид модели #######################################
        self.model_input_frame.grid(row=2, column=0, sticky=NSEW, padx=10, pady=10, ipady=5)
        self.model_input_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        self.model_option.grid(     row=1, column=0, sticky=NSEW, padx=10)
        

        ################ 1.3 блок. Дополнительные параметры ##########################
        self.additional_input_label.grid(   row=3, column=0, sticky=W, padx=10, pady=5)
        self.model_button.grid(             row=5, column=0, sticky=SE, padx=10, pady=35)
        
        
        ############### 2 блок. Предварительный просмотр #############################
        self.preview_frame.grid(    row=0, column=1, sticky=NSEW)
        self.preview_frame.grid_columnconfigure(0, weight=4)
        self.previw_label.grid(     row=0, column=0, pady=20)
        self.preview_canvas.grid(   row=1, column=0, pady=20)
        self.accept_button.grid(    row=2, column=0, pady=10, padx=20, sticky=SE)

    def model_button_callback(self):
        try:
            w           = self.preview_canvas.weight = int(self.size_input_x.get())
            h           = self.preview_canvas.height = int(self.size_input_y.get())
            r           = int(self.additional_input_frame.input_r.get())
            delta_r     = int(self.additional_input_frame.input_delta.get())
            T           = int(self.additional_input_frame.input_T.get())
            a           = int(self.additional_input_frame.input_a.get())
            d           = int(self.additional_input_frame.input_D.get())
            n           = int(self.additional_input_frame.input_N.get())
            fps         = int(self.additional_input_frame.input_frames.get())
            time        = int(self.additional_input_frame.input_t.get())
            if (T < 1):
                raise Exception
        except:
            return
        
        self.preview_canvas.play = False

        self.preview_canvas.images = [] #Очистка буфера видеоизображений

        
        self.img = np.zeros((h, w, 3), np.uint8)

        x        =   float(self.additional_input_frame.input_i.get()) +  w / 2
        y        = - float(self.additional_input_frame.input_j.get()) +  h / 2
        
        if self.model_type == 'Задержанный единичный импульс':
            cv2.circle(self.img, (int(x), int(y)), 3,(255, 255, 255), -1)

        elif self.model_type == 'Задержанный единичный скачок':
            cv2.rectangle(self.img, (int(x), int(y)), (h, 0), (255, 255, 255), -1)

        elif self.model_type == 'Одиночный круг':
            self.preview_canvas.t = 0
            frames = [] # матрица картинок
            self.preview_canvas.play = True
            self.preview_canvas.fps  = fps / time
            out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M','J','P','G'), self.preview_canvas.fps, (w, h))
            

            for t in np.linspace(0, time, fps):
                r_t      = int(r + delta_r * np.cos(2 * np.pi * t / T))
                self.img = np.zeros((h, w, 3), np.uint8) # костыль, чтобы каждый раз на пустую матрицу делала картинку
                cv2.circle(self.img, (int(x), int(y)), r_t,(255, 255, 255), -1)
                frames.append(self.img)
                out.write(self.img)
                # print(r_t)

            out.release()
            self.preview_canvas.video = frames

        elif self.model_type == 'Одиночный квадрат':
            self.preview_canvas.t = 0
            frames = [] # матрица картинок
            self.preview_canvas.play = True
            self.preview_canvas.fps  = fps / time
            out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M','J','P','G'), self.preview_canvas.fps, (w, h))

            for t in np.linspace(0, time, fps):
                self.img    = np.zeros((h, w, 3), np.uint8)

                a_t         = a + delta_r * np.cos(2 * np.pi * t / T)
                print()
                x0          = int(x - a_t / 2) if ((x - a_t / 2) >  0) else 0
                x1          = int(x + a_t / 2) if ((x + a_t / 2) <= w) else w
                y0          = int(y - a_t / 2) if ((y - a_t / 2) >  0) else 0
                y1          = int(y + a_t / 2) if ((y + a_t / 2) <= h) else h
                
                self.img[y0 : y1, x0 : x1, :] = 255

                # self.img[ : x + a_t // 2, y - a_t // 2 : y + a_t // 2, 0] = 255
                frames.append(self.img)
                
                out.write(self.img)
                # print(r_t)

            out.release()
            self.preview_canvas.video = frames

        elif self.model_type == 'Шахматная доска':
            self.preview_canvas.weight = a * n
            self.preview_canvas.height = a * n
            self.img = np.zeros((self.preview_canvas.height, self.preview_canvas.weight, 3), np.uint8)
            colors = ((255, 255, 255), (0, 0, 0))

            for x in range(n):
                for y in range(n):
                    c = (y + x) & 1
                    x1 = x * a
                    y1 = y * a
                    x2 = x1 + a
                    y2 = y1 + a
                    cv2.rectangle(self.img, (x1, y1), (x2, y2), colors[c], -1)

        elif self.model_type == 'Круги в узлах прямоугольной решетки':
            self.preview_canvas.weight = ((n - 1) * d) + (2 * r)
            self.preview_canvas.height = ((n - 1) * d) + (2 * r)
            self.img = np.zeros((self.preview_canvas.height, self.preview_canvas.weight, 3), np.uint8)

            for x in range(n):
                for y in range(n):
                    x1 = x * d + r
                    y1 = y * d + r
                    # x2 = x1 + a - 2.0 * radius
                    # y2 = y1 + a - 2.0 * radius
                    cv2.circle(self.img, (x1, y1), r, (255, 255, 255), -1)

        elif self.model_type == 'Случайные круги':
            pass
        elif self.model_type == 'Белый шум с равномерным распределением':
            pass
        elif self.model_type == 'Белый шум с нормальным распределением':
            pass
        elif self.model_type == 'Плоская гравитационная волна':
            pass
                # cv2.imwrite(f'hmm{t}.jpg', self.img) # сохранить ряд картинок для проверки видео
            
        
        
        
        # self.root.after(int(1000 / 23), self.update)
        self.preview_canvas.img = self.img
        # self.update()

    def accept_button_callback(self):
        # image = cv2.imread('model.png')
        if self.preview_canvas.play:
            vid_model = cv2.VideoCapture('outpy.avi')
            VideoPlayerWindow(self.root, vid_model)
        else:
            PicWindow(self.root, 1024, 768, image_cv=self.img)
    
    def delayed_single_impulse(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_impulse()
    
    def delayed_single_hop(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_hop()

    def single_circle(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_circle()

    def single_square(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_square()
    
    def chessboard(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_chess()
    
    def circles_at_nodes(self):
        self.additional_input_frame.forget()
        self.additional_input_frame.grid_node_circles()
    
    def random_circles(self):
        pass
    
    def noise_uniform_distribution(self):
        pass
    
    def noise_normal_distribution(self):
        pass
    
    def flat_gravitational_wave(self):
        pass