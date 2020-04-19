#Created By Faraz Naseem.

#Pandas and Matplotlib are imported.
import pandas as pd
import matplotlib.pyplot as plt

def dowGraph():
    #the data_frame variable reads the excels spreadsheet.
    data_frame = pd.read_excel("stock_dates_data.xlsx")

    #The data is plotted.
    plt.plot(data_frame['Date'], data_frame['Close'])

    plt.xlabel("Date")
    plt.ylabel("Value")

    #The title of the Graph
    plt.title("Dow Jones Graph")


    #The graph is shown.
    plt.show()

dowGraph()
