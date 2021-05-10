import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from sub_pages import SubPages


class InvestmentOptionsPage2(SubPages):
    '''
    Displays a graph of how user should invest and specific amounts.

    Calculates and displays how much of users money should be allocated to investment
    and specifically which type if investment

    Attributes
    ----------
    widget : NoneType
        To be later used to draw and destory canvas for graph.

    Methods
    -------
    None

    '''

    def __init__(self, parent, controller):
        '''
        Initializes the InvestmentOptionsPage2 object.

        Uses user entered data to calculate allocation of investment money and plots it using
        matplotlib, then displays on tkinter window.

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
        self.widget = None
        userInfoFile = open("Data/User_Info.txt", "r")
        userInfo = []
        for line in userInfoFile:
            userInfo.append(line.rstrip("\n"))
        userInfoFile.close()
        userInfo[0] = float(userInfo[0])
        userInfo[1] = float(userInfo[1])
        userInfo[2] = float(userInfo[2])
        label1 = tk.Label(self, text=userInfo[3], font=("Arial", 24))
        label1.pack(pady=20, padx=20)
        slices = []
        percentages = []
        investments = []
        monthlyInvestMoney = userInfo[1]*(userInfo[2]/100)
        if userInfo[3] == "High Reward/High Risk":
            upfrontStocks = userInfo[0]*0.7
            upfrontBonds = userInfo[0]*0.2
            upfrontCash = userInfo[0]*0.1
            monthlyStocks = monthlyInvestMoney*0.7
            monthlyBonds = monthlyInvestMoney*0.2
            monthlyCash = monthlyInvestMoney*0.1
            slices = [70, 20, 10]
            percentages = ["70% Stocks", "20% Bonds", "10% Cash"]
            investments = ["First investment in Stocks: $"+str(upfrontStocks)+"\nMonthly investment in Stocks: $"+str(monthlyStocks),
                           "First investment in Bonds: $"+str(upfrontBonds)+"\nMonthly investment in Bonds: $"+str(monthlyBonds),
                           "First Cash investment: $"+str(upfrontCash)+"\nMonthly Cash investment: $"+str(monthlyCash)]
        elif userInfo[3] == "Medium Reward/MediumRisk":
            upfrontStocks = userInfo[0] * 0.5
            upfrontBonds = userInfo[0] * 0.35
            upfrontCash = userInfo[0] * 0.15
            monthlyStocks = monthlyInvestMoney * 0.5
            monthlyBonds = monthlyInvestMoney * 0.35
            monthlyCash = monthlyInvestMoney * 0.15
            slices = [50, 35, 15]
            percentages = ["50% Stocks", "35% Bonds", "15% Cash"]
            investments = ["First investment in Stocks: $" + str(upfrontStocks) + "\nMonthly investment in Stocks: $" + str(monthlyStocks),
                            "First investment in Bonds: $" + str(upfrontBonds) + "\nMonthly investment in Bonds: $" + str(monthlyBonds),
                            "First Cash investment: $" + str(upfrontCash) + "\nMonthly Cash investment: $" + str(monthlyCash)]
        elif userInfo[3] == "Low Reward/Low Risk":
            upfrontStocks = userInfo[0] * 0.35
            upfrontBonds = userInfo[0] * 0.4
            upfrontCash = userInfo[0] * 0.25
            monthlyStocks = monthlyInvestMoney * 0.35
            monthlyBonds = monthlyInvestMoney * 0.4
            monthlyCash = monthlyInvestMoney * 0.25
            slices = [35, 40, 25]
            percentages = ["35% Stocks", "40% Bonds", "25% Cash"]
            investments = ["First investment in Stocks: $" + str(upfrontStocks) + "\nMonthly investment in Stocks: $" + str(monthlyStocks),
                            "First investment in Bonds: $" + str(upfrontBonds) + "\nMonthly investment in Bonds: $" + str(monthlyBonds),
                            "First Cash investment: $" + str(upfrontCash) + "\nMonthly Cash investment: $" + str(monthlyCash)]

        if self.widget:
            self.widget.destroy()

        f = matplotlib.figure.Figure(figsize=(5, 5))
        p = f.add_subplot(111)
        p.pie(slices, labels=percentages)
        f.legend(investments)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        self.widget = canvas.get_tk_widget()
        self.widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)