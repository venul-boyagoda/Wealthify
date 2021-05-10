import tkinter as tk
from home_page import HomePage
from historical_stock_data_page import HistoricalStockDataPage
from companies_page import CompaniesPage
from predict_stock_price_page import PredictStockPricePage
from investment_options_page import InvestmentOptionsPage
from investment_options_page_2 import InvestmentOptionsPage2


class WealthifyApp(tk.Tk):
    '''
    The main application object which creates instances of each screen in the application.

    This initializes the main structure consistent between all pages on the GUI by having a
    dictionary containing each page which can be called when needed.

    Attributes
    ----------
    frames : dict
        A dictionary containing each pre-initialized page of the application.

    Methods
    -------
    showFrame()
        Raises an application screen to the front, creating an instance of that screen.

    '''

    def __init__(self):
        '''
        Initializes a WealthifyApp object.

        Creates a parent and controller class allowing it to be the root class for inheritance
        of tkinter widgets and classes.

        Parameters
        ----------
        None

        Returns
        -------
        None

        '''
        tk.Tk.__init__(self)

        tk.Tk.wm_title(self, "Wealthify")
        width, height = tk.Tk.winfo_screenwidth(self), tk.Tk.winfo_screenheight(self)
        tk.Tk.geometry(self, '%dx%d+0+0' % (width,height))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for i in (HomePage, HistoricalStockDataPage, CompaniesPage, PredictStockPricePage, InvestmentOptionsPage, InvestmentOptionsPage2):
            frame = i(container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame(HomePage)

    def showFrame(self, page):
        '''
        Raises an application screen to the front, creating an instance of that screen.

        Function does this by finding the frame required from the dictionary of all frames,
        then raises that one to the top.

        Parameters
        ----------
        page : str
            Contains the dictionary key for the frame that needs to be raised.

        Returns
        -------
        None

        '''
        frame = self.frames[page]
        frame.tkraise()