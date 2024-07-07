from flask import Flask, jsonify, render_template
import yfinance as yf

app = Flask(__name__)

STOCK_SYMBOL = 'ASTS'

def get_stock_price():
    stock = yf.Ticker(STOCK_SYMBOL)
    stock_info = stock.history(period="1d")
    return stock_info['Close'].iloc[-1]

@app.route('/price')
def price():
    price = get_stock_price()
    return jsonify({'price': price})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
