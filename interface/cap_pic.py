from  customtkinter import *
from settings.rgb_bw import Settings
from interface.widgets.settings import SettingsMenu
from interface.widgets.display import Output_display
from interface.widgets.switch_widget import MySwitch
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
        self.switch_var = StringVar(value='1')

        self.tab_view = CTkTabview(self.root)
        self.tab_view.add('Изображение')
        self.tab_view.add('Настройки')
        self.tab_view.pack()
        
        self.rgb_gray_switch = MySwitch(self.tab_view.tab('Изображение'),
                                        text='RGB-Gray',
                                        variable=self.switch_var,
                                        command=self.switch_callback)
        self.output_label = Output_display(self.tab_view.tab("Изображение"))         

        self.draw_widgets_main(self.tab_view.tab('Изображение'))
        self.settings_menu = SettingsMenu(self.tab_view.tab("Настройки"), [self.hmm.contrast, self.hmm.brightness, self.hmm.red, self.hmm.green, self.hmm.blue])
        self.settings_menu.pack()
              
    def focus(self):

        self.root.grab_set()
    
    def draw_widgets_main(self, tab_main):
        
        self.rgb_gray_switch.pack()
        self.output_label.draw_picture(self.image_cv)


    def switch_callback(self):
        
        if self.switch_var.get() == '1':
            img = self.hmm.gray()
            self.output_label.on_change(img)

        else:
            self.output_label.on_change(self.image_cv)