import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.ticker as plticker
from sub_pages import SubPages
from stock import Stock

class PredictStockPricePage(SubPages):
    '''
    Allows user to display the graph of price predictions for a stock.

    User can enter the ticker for any stock and using matplotlib, graph of predicted stock prices
    will be displayed.

    Attributes
    ----------
    widget : NoneType
        To be later used to draw and destory canvas for graph.
    toolbar : NoneType
        To be later used to draw and destory toolbar for graph.

    Methods
    -------
    graphStockPrediction()
        Plots and displays a graph of predicted stock prices.

    '''

    def __init__(self, parent, controller):
        '''
        Initializes the PredictStockPricePage object.

        Uses tkinter buttons and entry to allow user to enter which stock they would like to
        see a prediction of.

        Parameters
        ----------
        parent : obj
            Frame() object created when WealthifyApp is initialized.
        controller : obj
            WealthifyApp object used to switch between screens.

        Returns
        -------
        None

        '''
        SubPages.__init__(self, parent, controller)
        label = tk.Label(self, text="Predict Stock Prices", font=("Arial", 24))
        label.pack(pady=20, padx=20)
        self.widget = None
        self.toolbar = None

        entry = tk.Entry(self)
        entry.pack()
        button = ttk.Button(self, text="View Prediction graph", command=lambda: self.graphStockPrediction(entry.get()))
        button.pack()

    def graphStockPrediction(self, entry):
        '''
        Plots and displays a graph of predicted stock prices.

        Uses a list of predicted prices of the stock and plots them using matplotlib, then
        displays them on the tkinter window.

        Parameters
        ----------
        entry : str
            User's stock ticker entry

        Returns
        -------
        None

        '''
        stock = Stock(entry)
        datesAndPrices = stock.predictStockPrice()
        dates = datesAndPrices[0]
        prices = datesAndPrices[1]
        pricesRange = max(prices) - min(prices)

        if self.widget:
            self.widget.destroy()

        if self.toolbar:
            self.toolbar.destroy()

        f = Figure(figsize=(8, 3), dpi=100)
        p = f.add_subplot(111)
        p.cla()
        p.plot(dates[:(len(dates)-365)], prices[:(len(prices)-365)], color="blue", label="Actual Prices")
        p.plot(dates[(len(dates)-365):], prices[(len(prices)-365):], color="green", label="Predicted Prices")
        p.legend(loc="lower right", frameon=True, fancybox=True, borderpad=1, shadow=True)
        p.set_xlabel("Date/# Weeks Predicted")
        p.set_ylabel("Price($)")
        loc1 = plticker.MultipleLocator(len(dates)/20)
        loc2 = plticker.MultipleLocator(base=(pricesRange / 10))
        p.xaxis.set_major_locator(loc1)
        p.yaxis.set_major_locator(loc2)
        f.autofmt_xdate()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(canvas, self)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)