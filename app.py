from flask import Flask, request, jsonify, render_template
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_price', methods=['POST'])
def get_stock_price():
    stock_symbol = request.form['symbol']
    try:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.history(period="1d")
        if not stock_info.empty:
            current_price = stock_info['Close'].iloc[-1]
            return jsonify({'price': round(current_price, 2)})
        else:
            return jsonify({'error': 'Invalid stock symbol or no data available.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
