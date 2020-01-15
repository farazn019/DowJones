import yfinance as yf
import matplotlib.pyplot as plt

#This will display all the graphs of the 30 companies that constitute the Dow Jones Industrial Average.

def displayStock():
    download_data = yf.download('BA', '2019-01-01', '2019-10-10')
    download_data.Close.plot()
    plt.show()

