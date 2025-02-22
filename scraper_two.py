
from bs4 import BeautifulSoup
import requests


url = "https://finance.yahoo.com/quote/AAPL"

def get_apple_stock_data():
   
    response = requests.get(url)
    
   
    if response.status_code != 200:
        print(f"Failed to retrieve data: HTTP Status Code {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    try:
        current_price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text.strip()
        previous_close = soup.find('fin-streamer', {'data-field': 'regularMarketPreviousClose'}).text.strip()
        market_cap = soup.find('fin-streamer', {'data-field': 'marketCap'}).text.strip()

        print(f"Current Price of AAPL: ${current_price}")
        print(f"Previous Close: ${previous_close}")
        print(f"Market Cap: {market_cap}")

    except AttributeError:
        print("Failed to retrieve some of the data.")

if __name__ == "__main__":
    get_apple_stock_data()






