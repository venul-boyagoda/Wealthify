import tkinter as tk
from tkinter import ttk
from historical_stock_data_page import HistoricalStockDataPage
from companies_page import CompaniesPage
from predict_stock_price_page import PredictStockPricePage
from investment_options_page import InvestmentOptionsPage

class HomePage(tk.Frame):
    '''
    Home page object which is instantiated as soon as the program is run, directs to other pages.

    Changes the screen when the user presses a button by passing the choice to the controller class,
    allowing user to access all other screens from the HomePage object.

    Attributes
    ----------
    None

    Methods
    -------
    None

    '''

    def __init__(self, parent, controller):
        '''
        Initializes the HomePage object.

        Uses tkinter buttons, along with the parent class and the controller to allow user to
        navigate to whichever page they want.

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
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file="Icons/logo picture.png")
        label = tk.Label(self, image=logo)
        label.image = logo
        #label = tk.Label(self, text="Wealthify", font=("Arial", 24))
        label.pack(pady=20, padx=20)

        s = ttk.Style()
        s.configure("W.TButton", font=("Arial", "18", "bold"))
        historyIcon = tk.PhotoImage(file="Icons/history_icon1.png")
        button1 = ttk.Button(self, text="Find Historical Stock Prices", style="W.TButton", image=historyIcon, compound=tk.LEFT, command=lambda: controller.showFrame(HistoricalStockDataPage))
        button1.image = historyIcon
        button1.pack(pady=20)
        searchIcon = tk.PhotoImage(file="Icons/search_icon.png")
        button2 = ttk.Button(self, text="View/Find a Publicly Traded Company", style="W.TButton", image=searchIcon, compound=tk.LEFT, command=lambda: controller.showFrame(CompaniesPage))
        button2.image = searchIcon
        button2.pack(pady=20)
        predictIcon = tk.PhotoImage(file="Icons/predict_icon.png")
        button3 = ttk.Button(self, text="Predict Stock Prices", style="W.TButton",  image=predictIcon, compound=tk.LEFT, command=lambda: controller.showFrame(PredictStockPricePage))
        button3.image = predictIcon
        button3.pack(pady=20)
        investIcon = tk.PhotoImage(file="Icons/invest_icon.png")
        button4 = ttk.Button(self, text="Investment Options", style="W.TButton", image=investIcon, compound=tk.LEFT, command=lambda: controller.showFrame(InvestmentOptionsPage))
        button4.image = investIcon
        button4.pack(pady=20)
        exitIcon = tk.PhotoImage(file="Icons/exit_icon.png")
        button4 = ttk.Button(self, text="Quit", style="W.TButton", image=exitIcon, compound=tk.LEFT, command=quit)
        button4.image = exitIcon
        button4.pack(pady=20)