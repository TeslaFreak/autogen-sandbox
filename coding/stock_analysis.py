# filename: stock_analysis.py
import yfinance as yf
import matplotlib.pyplot as plt

# Get the stock data for NVDA and TSLA
nvda = yf.download("NVDA", start="2021-01-01")
tsla = yf.download("TSLA", start="2021-01-01")

# Plot the stock price change YTD
plt.plot(nvda['Close'], label='NVDA')
plt.plot(tsla['Close'], label='TSLA')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price Change YTD')
plt.legend()

# Display the chart
plt.show()