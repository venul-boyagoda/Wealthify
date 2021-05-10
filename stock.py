from alpha_vantage.timeseries import TimeSeries
import json
import numpy as np


class Stock:
    '''
    Stock object that holds the ticker of a stock.

    Using the stocks ticker, it can find historical prices of that stock and also predict
    future prices for stock.

    Attributes
    ----------
    ticker : str
        The ticker symbol of the stock.

    Methods
    -------
    historicalStockPrice() -> tuple
        Gets historical prices of a stock.
    predictStockPrice() -> tuple
        Predicts future prices of a stock.

    '''

    def __init__(self, ticker):
        '''
        Initializes and is the constructor to build Stock object.

        Parameters
        ----------
        ticker : str
            The ticker symbol of the stock.

        Returns
        -------
        None

        '''
        self.ticker = ticker

    def historicalStockPrice(self):
        '''
        Gets historical prices of a stock.

        Uses AlphaVantage API to access weekly historical stock prices, then saves that to file.
        File is read and the dates and closing prices of the stock are written to lists.

        Parameters
        ----------
        None

        Returns
        -------
        date, price : tuple
            Lists of dates and historical prices of stock.

        '''
        key = "YMZ1UOPBRA4ZDRKB"
        ts = TimeSeries(key)
        symbol = self.ticker
        data, meta = ts.get_weekly(symbol)

        stockFile = open("Data/Stock_Prices_Storage.json", "w")
        json.dump(data, stockFile)
        stockFile.close()

        with open('Data/Stock_Prices_Storage.json', 'r') as f:
            stockPrices = json.load(f)

        date = []
        price = []

        for i in stockPrices:
            date.append(i)
            price.append(stockPrices[i]["4. close"])

        return (date, price)

    def predictStockPrice(self):
        '''
        Predicts prices of a stock.

        Linear fits dates and historical prices of stock to create an equation for the line.
        This equation is then used to determine the stock prices in coming weeks.

        Parameters
        ----------
        None

        Returns
        -------
        date, price : tuple
            Lists of dates and prices of stock including predictions.

        '''
        datesAndPrices = self.historicalStockPrice()
        print(type(datesAndPrices))
        dates = datesAndPrices[0][::-1]
        pricesList = datesAndPrices[1][::-1]
        prices = []
        for item in pricesList:
            prices.append(float(item))
        for i in range(1, 366):
            dates.append(str(i))

        x = []
        for i in range(len(prices)):
            x.append(i)
        x = np.array(x)
        y = np.array(prices)
        z = np.polyfit(x, y, 1)
        m = z[0]
        b = z[1]

        for i in range(len(prices), len(prices)+365):
            predictedPrice = (m*i) + b
            prices.append(predictedPrice)

        return (dates, prices)