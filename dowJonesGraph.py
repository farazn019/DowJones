import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_excel("stock_dates_data.xlsx")

plt.plot(data_frame['Date'], data_frame['Close'])

plt.xlabel("Date")
plt.ylabel("Value")

plt.title("Dow Jones Graph")

plt.show()
