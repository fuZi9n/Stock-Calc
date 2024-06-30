import yfinance as yf

def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period='1d')
    return todays_data['Close'].iloc[0]

ticker_symbol = 'ASTS'
current_price = get_stock_price(ticker_symbol)
print(f"The current price of {ticker_symbol} is ${current_price:.2f}")
