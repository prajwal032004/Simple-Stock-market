# 📈 Real-Time Stock Portfolio App
A dynamic web application to manage your stock portfolio with real-time stock price data fetched using the Yahoo Finance API. The app allows you to add, edit, and delete stocks, track their value, and view the total portfolio value. It also includes a dark mode toggle for better user experience.

## 🚀 Features
Real-Time Stock Prices: Fetches live stock prices using Yahoo Finance.
Add/Remove Stocks: Easily add stocks by symbol and quantity.
Dynamic Total Calculation: Automatically calculates the total portfolio value.
Dark Mode Toggle: Switch between light and dark mode for comfort.
Responsive Design: Works seamlessly on both desktop and mobile devices.
## 🛠️ Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Flask
APIs: Yahoo Finance (via yfinance library)
Styling: Custom CSS for clean and modern UI
## Access the website:
Open your browser and go to:

http://127.0.0.1:5000
## 📄 Dependencies	
requirements.txt

makefile
Copy code

Flask==3.0.3

requests==2.31.0

yfinance==0.2.38

pandas==2.2.2

Install dependencies using:

Copy code

pip install -r requirements.txt
## 💻 Project Structure
Copy code

real-time-stock-portfolio/

│-- static/

│   └── styles.css

│-- templates/

│   └── index.html

│-- app.py

│-- requirements.txt

└── README.md

## 🔧 How It Works
Frontend:

The user enters a stock symbol (e.g., AAPL) and a quantity.
The interface displays real-time stock prices and calculates the total value dynamically.
Dark mode can be toggled for better viewing.

Backend:

Flask handles the server-side logic.
Fetches real-time stock prices via the Yahoo Finance API (yfinance library).
Sends the data to the frontend for display.

## 🌟Modes
Light Mode

Dark Mode

## 🤝 Contributing
Contributions are welcome! Please open an issue first to discuss what you’d like to change.

Fork the repository.

Create a new branch (feature-branch).

Make your changes and commit them.

Submit a pull request.

## 📬 Contact
Name: Prajwal A B

GitHub: @prajwal032004

Happy coding! 🚀📈
