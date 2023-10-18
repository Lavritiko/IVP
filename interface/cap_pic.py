from  customtkinter import *
from settings.rgb_bw import Settings
from interface.widgets.settings import Settings_block
from interface.widgets.display import Output_display
from interface.widgets.switch_widget import Switch
from settings.rgb_bw import Settings

class PicWindow:
    def __init__(self, parent, width, height, image_cv=None, title='Child', resizable=(False, False)):
        
        self.root = CTkToplevel(parent)
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root.configure(background='gray22')
        
        self.focus()
        
        self.image_cv = image_cv
        self.hmm = Settings(self.image_cv)
        self.switch_var = StringVar(value='off')

        self.tab_view = CTkTabview(self.root)
        self.tab_view.add('Изображение')
        self.tab_view.add('Настройки')
        self.tab_view.pack()
        
        self.rgb_gray_switch = Switch(self.tab_view.tab('Изображение'), 'RGB-Gray')
        self.output_label = Output_display(self.tab_view.tab("Изображение"))         

        self.draw_widgets_main(self.tab_view.tab('Изображение'))
        self.draw_widgets_settings(self.tab_view.tab("Настройки"))
              
    def focus(self):

        self.root.grab_set()
    
    def draw_widgets_main(self, tab_main):
        
        self.rgb_gray_switch.draw_switch(self.switch_var, self.switch_callback)
        self.output_label.draw_picture(self.image_cv)       
    
    def draw_widgets_settings(self, tab_settings):

        Settings_block(tab_settings, 'Интенсивность').draw_slider(-127, 127, command=self.hmm.contrast)
        Settings_block(tab_settings, 'Яркость').draw_slider(-127, 127, command=self.hmm.brightness)
        Settings_block(tab_settings, 'Красный').draw_slider(-127, 127, command=self.hmm.red)
        Settings_block(tab_settings, 'Зеленый').draw_slider(0, 100)
        Settings_block(tab_settings, 'Синий').draw_slider(0, 100)

    def switch_callback(self):
        
        if self.switch_var.get() == 'on':
            img = self.hmm.gray()
            print(img)
            self.output_label.on_change(img)

        else:
            self.output_label.on_change(self.image_cv)