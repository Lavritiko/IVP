from  customtkinter import *
from settings.rgb_bw import Settings
from PIL import Image
from PIL import ImageTk

class PicWindow:
    def __init__(self, parent, width, height, image, image_cv=None, title='Child', resizable=(False, False)):
        self.root = CTkToplevel(parent)
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root.configure(background='gray22')
        self.widgets = []
        self.focus()

        self.tab_view = CTkTabview(self.root)
        self.tab_view.add('Изображение')
        self.tab_view.add('Настройки')

        self.image = image
        self.label = CTkLabel(self.tab_view.tab("Изображение"))
        self.label.configure(image=image, text='')
        self.label.image=image
        self.draw_widgets()
        self.hmm = Settings()
        self.image_cv = image_cv

    def focus(self):
        self.root.grab_set()
    
    
    def draw_widgets(self):
        print('hui')
        self.tab_view.pack()
        self.switch_var = StringVar(value='off')
        sw = CTkSwitch(self.tab_view.tab("Изображение"), text='Switch', command=self.switch_callback, variable=self.switch_var, width=150, height=30, onvalue='on', offvalue='off')
        sw.pack()
        self.label.pack()

        labdel_int = CTkLabel(self.tab_view.tab("Настройки"), text='Интенсивность')
        labdel_int.pack(pady=10)
        slider1 = CTkSlider(self.tab_view.tab("Настройки"), from_=0, to=100)
        slider1.pack(pady=10)

        labdel_bright = CTkLabel(self.tab_view.tab("Настройки"), text='Яркость')
        labdel_bright.pack(pady=10)
        slider2 = CTkSlider(self.tab_view.tab("Настройки"), from_=0, to=100)
        slider2.pack(pady=10)

        labdel_R = CTkLabel(self.tab_view.tab("Настройки"), text='Красный')
        labdel_R.pack(pady=10)
        slider_R = CTkSlider(self.tab_view.tab("Настройки"), from_=0, to=100)
        slider_R.pack(pady=10)

        labdel_G = CTkLabel(self.tab_view.tab("Настройки"), text='Зеленый')
        labdel_G.pack(pady=10)
        slider_G = CTkSlider(self.tab_view.tab("Настройки"), from_=0, to=100)
        slider_G.pack(pady=10)

        labdel_G = CTkLabel(self.tab_view.tab("Настройки"), text='Синий')
        labdel_G.pack(pady=10)

        slider_B = CTkSlider(self.tab_view.tab("Настройки"), from_=0, to=100)
        slider_B.pack(pady=10)

    def switch_callback(self):
        if self.switch_var.get() == 'on':
            img = self.hmm.gray(self.image_cv)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)
            self.label.configure(image=img)
            self.label.image=img
        else:
            self.label.configure(image=self.image)
            self.label.image=self.image