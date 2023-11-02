from  customtkinter import *
from interface.widgets.settings import SettingsMenu
from interface.widgets.pictute_screen import Output_display
from interface.widgets.switch_widget import Switch
from settings.rgb_bw import GraySettings, Gray

class PicWindow:
    def __init__(self, parent, width, height, image_cv=None, title='Child', resizable=(False, False)):
        
        self.root = CTkToplevel(parent)
        self.root.title(title)
        self.root.resizable(resizable[0], resizable[1])
        self.root.configure(background='gray22')
        
        self.focus()
        
        self.image_cv = image_cv
        self.gray_old = GraySettings(self.image_cv)
        self.switch_var = StringVar(value='off')

        self.tab_view = CTkTabview(self.root)
        self.tab_view.add('Изображение')
        self.tab_view.add('Настройки')
        self.tab_view.pack()
        
        self.rgb_gray_switch = Switch(self.tab_view.tab('Изображение'), 'RGB-Gray')
        self.output_label = Output_display(self.tab_view.tab("Изображение"))         
        self.grey = Gray()
        self.draw_widgets_main(self.tab_view.tab('Изображение'))
        self.settings_menu = SettingsMenu(self.tab_view.tab("Настройки"), [self.gray_old.contrast, self.gray_old.brightness, self.gray_old.red, self.gray_old.green, self.gray_old.blue])
        self.settings_menu.pack()
              
    def focus(self):

        self.root.grab_set()
    
    def draw_widgets_main(self, tab_main):
        
        self.rgb_gray_switch.draw_switch(self.switch_var, self.switch_callback)
        self.output_label.draw_picture(self.image_cv)


    def switch_callback(self):
        
        if self.switch_var.get() == 'on':
            # img = self.hmm.gray()
            self.grey.blue = self.settings_menu.blue
            self.grey.red = self.settings_menu.red
            self.grey.green = self.settings_menu.green
            self.grey.alpha_br = self.settings_menu.brightness
            self.grey.beta_cnt = self.settings_menu.intensity

            img = self.grey.hmm2(self.image_cv)
            print(img)
            self.output_label.on_change(img)

        else:
            self.output_label.on_change(self.image_cv)


    # def switch_callback(self):
        
    #     if self.switch_var.get() == 'on':
    #         img = self.gray.gray()
    #         print(img)
    #         self.output_label.on_change(img)

    #     else:
    #         self.output_label.on_change(self.image_cv)