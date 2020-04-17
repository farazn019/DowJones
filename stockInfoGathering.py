#This gathers the stock data, and inserts it into a spreadsheet.
import pandas as pd
import datetime
import yfinance as yf

#This function gathers all the stock information for the Dow Jones Industrial Average.
def dowJonesInformation():

    today = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day) #The exact date one year from today.
    last_year = str(datetime.datetime.now().year - 1) + '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day) #Today's date
    DJI = yf.download("DJI", last_year, today) #The 'DJI' variable stores all the data from the index fund, from last year to this year.
    

    
    priceToExcel = pd.ExcelWriter("stock_dates_data.xlsx", engine="xlsxwriter")
    DJI.to_excel(priceToExcel, sheet_name="stock_dates_data.xlsx", startcol=1)
    priceToExcel.save() #The data is saved.
    
        

dowJonesInformation()

