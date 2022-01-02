# Description: Stock market dashbaord

import streamlit as st
import pandas as pd
from PIL import Image

st.write(""
         "# **Stock market web app**")

image = Image.open("/home/allgiftali/Pictures/finance_img.jpg")
st.image(image, use_column_width=True)


#create a sidebar header
st.sidebar.header('User input')

# create a function to get the user input
def get_input():
    start_date = st.sidebar.text_input('Start Date', "2020-01-02")
    end_date = st.sidebar.text_input('End Date', "2020-08-02")
    sticker = st.sidebar.text_input('Sticker', "AMZN")
    return start_date, end_date, sticker


# create a function to get the company name
def get_company_name(sticker):
    if sticker == 'AMZN':
        return 'Amazon'
    elif sticker == 'TSLA':
        return 'Tesla'
    elif sticker == 'GOOG':
        return 'Alphabet'
    else:
        'None'


#create a function to get data and function
def get_data(sticker, start, end):

    # Load the data
    if sticker.upper() == 'AMZN':
        df = pd.read_csv("data/AMZN.csv")
    elif sticker.upper() == 'TSLA':
        df = pd.read_csv("data/tsla.csv")
    elif sticker.upper() == 'GOOG':
        df = pd.read_csv("data/goog.csv")
    else:
        df = pd.DataFrame(columns=['Date', 'Close', 'Open', 'Volume', 'Adj Close', 'High', 'Low'])


    # Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)


    # Set the start and the end index rows both to 0
    start_row = 0
    end_row = 0

    #Start the date from the top of the data set
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break

    # Start from the bottom of the data
    for j in range(0, len(df)):
        if end >= pd.to_datetime((df['Date'][len(df)-1-j])):
            end_row = len(df) -1 -j
            break

    #Set the index to the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row+1, :]

# Get the users input
start, end, sticker = get_input()

# Get the data
df = get_data(sticker, start, end)

#Get the company name
company_name = get_company_name(sticker.upper())

# Display the close price
st.header(company_name+" Close Price \n")
st.line_chart(df['Close'])
st.header(company_name+" Volume \n")
st.line_chart(df['Volume'])

#Get some statistics on the data
st.header('Data Statistics')
st.write(df.describe())