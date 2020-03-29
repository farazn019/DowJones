#Created By Faraz Naseem....

from tkinter import *
from StockNames import dowStocks
import matplotlib.pyplot as plt #This command just imports matplotlib.pyplot, and not the entire library.
import matplotlib #This command imports the entire matplotlib library.
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import yfinance as yf
import datetime
from dateutil import rrule
import random
import numpy as np

matplotlib.use("TKAgg")





def root():
    main_window = Tk()
    main_window.title("Dow Jones")
    main_window.geometry('1200x1200')
    
    today = datetime.datetime.now()
    last_year = today.year() - 1
    last_year_date = str(last_year + today.month() + today.day)
    current_date = str(today.year) + '-' + str(today.month) + '-' + str(today.day)
    yearly_date = []
    '''
    for dt in rrule.rrule(rrule.DAILY, dtstart = datetime.strptime(today, "%Y%m%d"), until = datetime.strptime(current_date, "%Y%m%d"))):
        yearly_date.append(dt)
    download_data = yf.download("DJI", '2019-01-01', str(current_date))
    
    
    figure = Figure(figsize=(1, 1), dpi = 100)
    a = figure.add_subplot(111)

    
    a.plot(x, y)

    canvas = FigureCanvasTkAgg(figure, master=main_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side="right")
    '''    

def subtitle():
    subtitle_frame = Frame(width = 300, height = 50)
    subtitle_frame.place(x = 150, height = 50)
    primary_subtitle = Label(subtitle_frame, text = "Dow Jones Industrial Average Stock Graph", fg = "red", bg = "blue", font = ("Times New Roman", 18, 'bold'))
    primary_subtitle.pack()




today = datetime.datetime.now()
current_date = str(today.year) + '-' + str(today.month) + '-' + str(today.day)

counter = 0

class dowStock():   
    def __init__(self, home_page, stock_code, stock_name, posx, posy):
        def addStock():
            global counter
            counter = counter + 1
            download_data = yf.download(stock_name, '2019-01-01', current_date)
            download_data.Close.plot(label = stock_name)
            if(counter == 1):
                plt.title("Value Of Stock")
            elif(counter > 1):
                plt.title("Value Of Stocks")
            plt.xlabel("Date")
            plt.ylabel("Value")
            plt.legend()
            plt.show()
            


        self.home_page = home_page
        self.stock_code = Button(home_page, text = stock_name, fg = "blue", bg = "red", font=("Arial", 7, "bold"), command = addStock)
        self.stock_code.place(x = posx, y = posy)
        self.stock_name = stock_name
        self.posx = posx





def main():

    root()
    subtitle()

    frame = Frame(width = 140, height = 600, bg = "black")
    frame.place(x = 0, y = 0)

    row = 0
    column = 0
    
    

    for key in dowStocks:
        val = dowStocks[key]
        column += 19
        stock = dowStock(frame, val, key, row, column)
    
    
    frame.mainloop()


main()
