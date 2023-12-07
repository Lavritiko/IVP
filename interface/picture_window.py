from  customtkinter import *
from interface.widgets.settings import SettingsMenu
from interface.widgets.picture_screen import Output_display
from interface.widgets.switch_widget import MySwitch
from settings.rgb_bw import Settings
from settings.rgb_bw import gray

class PicWindow:
    def __init__(self, parent, width, height, image_cv=None, title='Child', resizable=(False, False)):
        
        self.image_cv = image_cv

        self.root = CTkToplevel(parent)
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root.configure(background='gray22')
        
        # ========================== Create wigets ==========================

        self.tab_view = CTkTabview(self.root, command=self.select_menu)
        self.tab_view.add('Изображение')
        self.tab_view.add('Настройки')
        
        self.output_picture = Output_display(self.tab_view.tab("Изображение"), image_cv)

        self.switch_var = StringVar(value='1')
        
        self.rgb_gray_switch = MySwitch(self.tab_view.tab('Изображение'),
                                        text='RGB-Gray',
                                        variable=self.switch_var,
                                        command=self.switch_callback)
        
                           
        self.settings_menu = SettingsMenu(self.tab_view.tab("Настройки"))
        
        self.draw_widgets()
                 
    
    def draw_widgets(self):
        self.root.grab_set()
        self.tab_view.pack()
        
        # =============== Изображение ========================

        self.rgb_gray_switch.pack()
        self.output_picture.pack()

        # =============== Настройки ========================

        self.settings_menu.pack()

    def select_menu(self):
        if self.switch_var.get() == '1':
            self.rgb_gray_switch.toggle()

    def switch_callback(self):
        
        if self.switch_var.get() == '1':
            self.output_picture.is_gray = True
            self.output_picture.br  = self.settings_menu.brightness
            self.output_picture.cnt = self.settings_menu.intensity
            self.output_picture.r   = self.settings_menu.red
            self.output_picture.g   = self.settings_menu.green
            self.output_picture.b   = self.settings_menu.blue
            self.output_picture.on_change()

        else:
            self.output_picture.is_gray = False
            self.output_picture.on_change()
