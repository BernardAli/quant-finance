import numpy as np
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
from matplotlib import pyplot as plt
from datetime import timedelta, date
from scipy import optimize as sco
import tkinter as tk
from tkinter import filedialog

plt.style.use('seaborn')

sticker = ['^GSPC', '^DJI', '^IXIC', '^N225', '^STOXX50E']
years_no = int(input('Enter Number of years to get results'))
start_date = date.today() - timedelta(days=(252*int(years_no)))
end_date = date.today()

data = web.DataReader(sticker, data_source='yahoo', start=start_date, end=end_date)['Adj Close']

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()


def exportCSV():
    global data

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    data.to_csv(export_file_path, header=True)


saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=saveAsButton_CSV)

root.mainloop()