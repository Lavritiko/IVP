from  customtkinter import *
from settings.rgb_bw import image_statistics, IS_UPDATE_FUCKING_STATISTICS
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import cv2
from .widgets.video_screen import VideoScreen
import csv

class StatisticsWindow:
    def __init__(self, parent, gray_image, title='Статистика', resizable=(False, False), func=None):
        self.is_update = False
        self.gray_image = gray_image
        self.root = CTkToplevel(parent)
        self.root.title(title)
        self.root.geometry("850x400")
        self.root.resizable(resizable[0], resizable[1])
        self.func = func

        self.mean, self.std_dev, self.kurt, self.skewness, self.minimum, self.maximum, self.quantile5, self.quantile95 = image_statistics(self.gray_image)

        # ========================== Create wigets ==========================
        self.label_mean                  = CTkLabel(self.root, text='Среднее:', font=('Arial', 14), text_color='white')
        self.value_mean                  = CTkLabel(self.root, text=f'{self.mean: .2f}', font=('Arial', 14), text_color='white')

        self.label_variance              = CTkLabel(self.root, text='Дисперсия:', font=('Arial', 14), text_color='white')
        self.value_variance              = CTkLabel(self.root, text=f'{self.std_dev ** 2: .2f}', font=('Arial', 14), text_color='white')
        
        self.label_standart_deviation    = CTkLabel(self.root, text='Среднеквадратичное отклонение:', font=('Arial', 14), text_color='white')
        self.value_standart_deviation    = CTkLabel(self.root, text=f'{self.std_dev: .2f}', font=('Arial', 14), text_color='white')
        
        self.label_variation_coefficient = CTkLabel(self.root, text='Коэффициент вариации:', font=('Arial', 14), text_color='white')
        self.value_variation_coefficient = CTkLabel(self.root, text=f'{self.std_dev / self.mean: .2f}', font=('Arial', 14), text_color='white')
        
        self.label_skewness_coefficient  = CTkLabel(self.root, text='Коэффициент ассиметрии:', font=('Arial', 14), text_color='white')
        self.value_skewness_coefficient  = CTkLabel(self.root, text=f'{self.skewness: .2f}', font=('Arial', 14), text_color='white')
        
        self.label_kurtosis_coefficient  = CTkLabel(self.root, text='Коэффициент эксцесса:', font=('Arial', 14), text_color='white')
        self.value_kurtosis_coefficient  = CTkLabel(self.root, text=f'{self.kurt: .2f}', font=('Arial', 14), text_color='white')
        
        self.label_min                   = CTkLabel(self.root, text='Минимум:', font=('Arial', 14), text_color='white')
        self.value_min                   = CTkLabel(self.root, text=f'{self.minimum}', font=('Arial', 14), text_color='white')
        
        self.label_max                   = CTkLabel(self.root, text='Максимум:', font=('Arial', 14), text_color='white')
        self.value_max                   = CTkLabel(self.root, text=f'{self.maximum}', font=('Arial', 14), text_color='white')
        
        self.label_quantile_5            = CTkLabel(self.root, text='Квантиль порядка 0.05:', font=('Arial', 14), text_color='white')
        self.value_quantile_5            = CTkLabel(self.root, text=f'{self.quantile5: .2f}', font=('Arial', 14), text_color='white')
        
        self.label_quantile_95           = CTkLabel(self.root, text='Квантиль порядка 0.95:', font=('Arial', 14), text_color='white')
        self.value_quantile_95           = CTkLabel(self.root, text=f'{self.quantile95: .2f}', font=('Arial', 14), text_color='white')

        #Histogram
        self.figure = plt.Figure(figsize=(5, 3), dpi=100)
        self.ax = self.figure.add_subplot(111)

        self.hist_canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.hist_canvas.get_tk_widget().grid(row=0, column=3, rowspan=10, padx=10, pady=5)
        histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        self.ax = self.figure.gca()
        x = np.linspace(0, 255, 256)
        hist = max(histogram)
        hist *= (1 + 70/100)
        y = np.linspace(10, hist, 256)
        self.graph, = self.ax.plot(x, y)
        # self.ax.set_yscale('log')

        # запись в файл
        file = open('data.csv', 'w')
        self.writer = csv.writer(file)
        self.writer.writerow(['Mean', 'Variance', 'Standart deviation', 'Variation coefficient', 'Skewness coefficient', 'Kurtosis coefficient', 'Minimum','Maximum', 'Quantile  0.05', 'Quantile 0.95'])
        
        self.draw_widgets()
        # self.delay = 15
      
        # self.update()
        # self.check_update()
    def draw_widgets(self):
        self.label_mean.grid(row=0, column=0, sticky=W, padx=10, pady=5)
        self.value_mean.grid(row=0, column=1, sticky=W, padx=10, pady=5)
        
        self.label_variance.grid(row=1, column=0, sticky=W, padx=10, pady=5)
        self.value_variance.grid(row=1, column=1, sticky=W, padx=10, pady=5)

        self.label_standart_deviation.grid(row=2, column=0, sticky=W, padx=10, pady=5)
        self.value_standart_deviation.grid(row=2, column=1, sticky=W, padx=10, pady=5)
        
        self.label_variation_coefficient.grid(row=3, column=0, sticky=W, padx=10, pady=5)
        self.value_variation_coefficient.grid(row=3, column=1, sticky=W, padx=10, pady=5)

        self.label_skewness_coefficient.grid(row=4, column=0, sticky=W, padx=10, pady=5)
        self.value_skewness_coefficient.grid(row=4, column=1, sticky=W, padx=10, pady=5)

        self.label_kurtosis_coefficient.grid(row=5, column=0, sticky=W, padx=10, pady=5)
        self.value_kurtosis_coefficient.grid(row=5, column=1, sticky=W, padx=10, pady=5)

        self.label_min.grid(row=6, column=0, sticky=W, padx=10, pady=5)
        self.value_min.grid(row=6, column=1, sticky=W, padx=10, pady=5)

        self.label_max.grid(row=7, column=0, sticky=W, padx=10, pady=5)
        self.value_max.grid(row=7, column=1, sticky=W, padx=10, pady=5)
        
        self.label_quantile_5.grid(row=8, column=0, sticky=W, padx=10, pady=5)
        self.value_quantile_5.grid(row=8, column=1, sticky=W, padx=10, pady=5)

        self.label_quantile_95.grid(row=9, column=0, sticky=W, padx=10, pady=5)
        self.value_quantile_95.grid(row=9, column=1, sticky=W, padx=10, pady=5)
        self.calc_hist(self.gray_image)

    def update(self, gray=None):
        if gray is not None:
            self.gray_image = gray
        self.mean, self.std_dev, self.kurt, self.skewness, self.minimum, self.maximum, self.quantile5, self.quantile95 = image_statistics(self.gray_image)
        self.calc_hist(self.gray_image)
        self.value_mean.configure(text='{:.2f}'.format(self.mean))
        self.value_variance.configure(text='{:.2f}'.format(self.std_dev ** 2))
        self.value_standart_deviation.configure(text='{:.2f}'.format(self.std_dev))
        self.value_variation_coefficient.configure(text='{:.2f}'.format(self.std_dev / self.mean))
        self.value_kurtosis_coefficient.configure(text='{:.2f}'.format(self.kurt))
        self.value_skewness_coefficient.configure(text='{:.2f}'.format(self.skewness))
        self.value_min.configure(text='{:.2f}'.format(self.minimum))
        self.value_max.configure(text='{:.2f}'.format(self.maximum))
        self.value_quantile_5.configure(text='{:.2f}'.format(self.quantile5))
        self.value_quantile_95.configure(text='{:.2f}'.format(self.quantile95))
        # self.writer.writerow(['{:.2f}'.format(self.mean), 
                            #   '{:.2f}'.format(self.std_dev ** 2), 
                            #   '{:.2f}'.format(self.std_dev), 
                            #   '{:.2f}'.format(self.std_dev / self.mean), 
                            #   '{:.2f}'.format(self.kurt), 
                            #   '{:.2f}'.format(self.skewness), 
                            #   '{:.2f}'.format(self.minimum), 
                            #   '{:.2f}'.format(self.maximum), 
                            #   '{:.2f}'.format(self.quantile5), 
                            #   '{:.2f}'.format(self.quantile95)])

    # def check_update(self):
    #     global IS_UPDATE_FUCKING_STATISTICS
    #     if IS_UPDATE_FUCKING_STATISTICS[0]:
    #         self.gray_image = self.func
    #         self.update()
    #         IS_UPDATE_FUCKING_STATISTICS[0] = False
    #     self.root.after(self.delay, self.check_update)

    def calc_hist(self, gris):
        histogram = cv2.calcHist([gris], [0], None, [256], [0, 256])
        self.graph.set_ydata(histogram)
        self.hist_canvas.draw()
        self.writer.writerow(['{:.2f}'.format(self.mean), 
                              '{:.2f}'.format(self.std_dev ** 2), 
                              '{:.2f}'.format(self.std_dev), 
                              '{:.2f}'.format(self.std_dev / self.mean), 
                              '{:.2f}'.format(self.kurt), 
                              '{:.2f}'.format(self.skewness), 
                              '{:.2f}'.format(self.minimum), 
                              '{:.2f}'.format(self.maximum), 
                              '{:.2f}'.format(self.quantile5), 
                              '{:.2f}'.format(self.quantile95)])
        