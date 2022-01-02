# Description: Stock market dashbaord

import streamlit as st
import pandas_datareader.data as web
import pandas as pd
from PIL import Image
import yfinance as yf

st.write(""
         "# **Stock market web app**")

image = Image.open("/home/allgiftali/Pictures/finance_img.jpg")
st.image(image, use_column_width=True)


#create a sidebar header
st.sidebar.header('User input')

start_date = st.sidebar.text_input('Start Date', "2020-01-02")
end_date = st.sidebar.text_input('End Date', "2020-08-02")
sticker = st.sidebar.text_input('Sticker', "AMZN")


df = web.DataReader(sticker, data_source='yahoo', start=start_date, end=end_date)

company_name = str(sticker)


# Display the close price
st.header(company_name+" Close Price \n")
st.line_chart(df['Close'])
st.header(company_name+" Volume \n")
st.bar_chart(df['Volume'])

#Get some statistics on the data
st.header('Data Statistics')
st.write(df.describe())

#Get some details on the data
st.header('Company Details')
details = yf.Ticker(company_name)
st.write(details.info['longBusinessSummary'])