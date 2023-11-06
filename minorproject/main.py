import gradio as gr
import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np


# Function to train a simple stock prediction model
def train_stock_model(stock_symbol, start_date, end_date):
    # Download historical stock data using Yahoo Finance
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Calculate daily returns
    stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()

    # Drop missing values
    stock_data.dropna(inplace=True)

    # Define features and target
    X = np.array(stock_data['Close']).reshape(-1, 1)
    y = stock_data['Daily_Return']

    # Train a simple Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    return model


# Function to predict stock returns
def predict_stock_returns(model, stock_price):
    return model.predict(np.array(stock_price).reshape(-1, 1))


# Create a Gradio interface
def stock_prediction_chat_bot():
    stock_symbol = gr.inputs.Text(label="Stock Symbol (e.g., AAPL)")
    start_date = gr.inputs.Date(label="Start Date")
    end_date = gr.inputs.Date(label="End Date")
    stock_price = gr.inputs.Number(label="Stock Price (today's)")

    model = train_stock_model(stock_symbol, start_date, end_date)
    prediction = predict_stock_returns(model, stock_price)

    return round(prediction[0], 4)


iface = gr.Interface(fn=stock_prediction_chat_bot,
                     inputs=["Stock Symbol", "Start Date", "End Date", "Stock Price"],
                     outputs="text")
iface.launch()
