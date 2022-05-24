import os
import requests
import csv
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["api_key"]

class StockAPI:
    techStock = {
            'Apple': 'AAPL',
            'Amazon': 'AMZN',
            'Netflix': 'NFLX',
            'Facebook': 'META',
            'Google': 'GOOG'
    }

    def getStockData(self, symbol : str, apiKey=API_KEY):
        """
        Returns the Stock Data for each symbol passed symbol.

        Parameters:
            symbol (str):The symbol of stock for which stock price to be return.
            apiKey : User Registered API key, passed via .env file
        
        Returns:
            r (json): Stock data in json format. 
        """
        try:
            base_url = 'https://finnhub.io/api/v1//quote?'
            headers = {'X-Finnhub-Token': apiKey}
            r = requests.get(base_url, params = {'symbol': symbol}, headers=headers)
            return r.json()
        except Exception as err:
            print(f'Error Getting Stock Data: {err}')

    def getTechStocks(self, stocks: list):
        """
        Returns Dictionary of Stock Data for all the stock as key-value pair.

        Parameters:
            stock (list): The list of company name whose stock prices has to be returned
        
        Returns:
            stockDetail (dict) : Stock Data for the company requested for. 
        """
        stockDetail = dict()
        for stock in stocks:
            symbol = self.techStock.get(stock)
            stockDetail[symbol] = self.getStockData(symbol)
        return stockDetail

    def getLatestPrice(self, stocks: dict):
        """
        Returns Only the Latest Price for all the stocks requested

        Parameters:
            stock (dict): Stock Data for the company requested for. 
        
        Returns:
            latestPrices (dict) : Latest Price for each company stock. 
        """
        latestPrices = dict()
        for stock, prices in stocks.items():
            latestPrices[stock] = prices.get('c')
        return latestPrices

    def getMostVolatileStock(self, stocks: dict):
        """
        Returns the Most Volatile stock(that moved the most percentage points from yesterday).

        Parameters:
            stocks (dict): Stock data dictionary with all stock data.
        
        Returns:
            dict: Most Volatile Stock with Percent change, current price and Last Clost Price. 
        """
        mostVolatile = {'stock_symbol': None, 
            'percentage_change': 0, 
            'current_price': 0, 
            'last_close_price': 0
        }

        for stock, prices in stocks.items():
            cPrice = prices.get('c')
            lcPrice = prices.get('pc')
            try:
                pChange = ((cPrice - lcPrice) / abs(lcPrice)) * 100
            except Exception as err:
                print(f'Cannot Generate Percentage Change for {stock} as error: {err}')
                continue

            if pChange > mostVolatile.get('percentage_change'):
                mostVolatile['stock_symbol'] = stock
                mostVolatile['percentage_change'] = pChange
                mostVolatile['current_price'] = cPrice
                mostVolatile['last_close_price'] = lcPrice
            
        return mostVolatile

    def getCSV( self, mostVolatileStock: dict):
        """
        Generates a CSV file for the most volatile stock.

        Parameters:
            mostVolatileStock (dict): Most Volatile Stock with Percent change, current price and Last Clost Price. 
        """
        try:
            with open('MostVolatileStock.csv', 'w') as f: 
                writer = csv.DictWriter(f, fieldnames=mostVolatileStock.keys())
                writer.writeheader()
                writer.writerow(mostVolatileStock)
                #print("CSV Generated")
        except Exception as err:
            print(f'Error Generating CSV File - Error: {err}')


if __name__ == "__main__":
    sp = StockAPI()
    price = sp.getTechStocks(['Apple',  'Amazon', 'Netflix', 'Facebook', 'Google'])

    #Print Latest Price
    print(f'Latest Price for : {sp.getLatestPrice(price)}')

    #Volatile Stock data
    volatileStock = sp.getMostVolatileStock(price)
    print(f'Most Volatile Stock is : {volatileStock}')
    sp.getCSV(volatileStock)


    
