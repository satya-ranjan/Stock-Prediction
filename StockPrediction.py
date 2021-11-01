import numpy as np
import pandas as pd

import streamlit as st
from datetime import date


import yfinance as yf

#from fbprophet import Prophet
#from fbprophet.plot import plot_plotly

from plotly import graph_objs as go
#import pandas_datareader as data


START = "2010-01-01"
TODAY = date.today().strftime("%Y-%m-%d")


st.title("Stock Prediction")

stocks = st.text_input("Enter Stock Ticker",'AAPL')
selected_stock = (stocks) 

n_years = st.slider("Year of prediction:", 1, 4)
period = n_years * 365

@st.cache
def load_data(ticker):
    data = yf.download(ticker, START,TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data..")
data = load_data(selected_stock)
data_load_state.text("Loading data...done!")

st.subheader('Raw data')
st.write(data.tail(10))

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Open'] , name = 'stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Close'] , name = 'stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'],y=data['High'] , name = 'High'))
    fig.add_trace(go.Scatter(x=data['Date'],y=data['Low'] , name = 'Low'))
    fig.layout.update(title_text="High-Low Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=data['High'],y=data['Low'] , name = 'High'))
    fig.add_trace(go.Histogram(x=data['High'],y=data['Low'] , name = 'Low'))
    fig.layout.update(title_text="High-Low Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['High'],y=data['Low'] , name = 'High'))
    fig.add_trace(go.Bar(x=data['High'],y=data['Low'] , name = 'Low'))
    fig.layout.update(title_text="High-Low Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()
