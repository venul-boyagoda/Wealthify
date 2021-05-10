import tkinter as tk
from tkinter import ttk
from sub_pages import SubPages
from investment_options_page_2 import InvestmentOptionsPage2

class InvestmentOptionsPage(SubPages):
    '''
    Allows user to enter their investment information/goals to be used later.

    User can enter information such as how much they are willing to invest, how much they
    earn monthly and how they want to build their investment portfolio using tkinter entry
    boxes and option menus.

    Attributes
    ----------
    None

    Methods
    -------
    userInfo()
        Stores information user has entered into a file.

    '''

    def __init__(self, parent, controller):
        '''
        Initializes the InvestmentOptionsPage object.

        Uses tkinter buttons and entry to allow user to enter their data on investment.

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
        label1 = tk.Label(self, text="Investment Options", font=("Arial", 24))
        label1.pack(pady=20, padx=20)
        label2 = tk.Label(self, text="Please enter the following information for a personalized investment plan.(Numbers only)", font=("Arial", 18))
        label2.pack(pady=20, padx=20)

        label3 = tk.Label(self, text="How much would you like to invest at first?(CAD)", font=("Arial", 14))
        label3.pack(pady=20, padx=20)
        entry1 = tk.Entry(self)
        entry1.pack()
        label4 = tk.Label(self, text="How much do you make in a month?(CAD)", font=("Arial", 14))
        label4.pack(pady=20, padx=20)
        entry2 = tk.Entry(self)
        entry2.pack()
        label4 = tk.Label(self, text="What percentage of your monthly salary would you like to invest?", font=("Arial", 14))
        label4.pack(pady=20, padx=20)
        entry3 = tk.StringVar(self)
        entry3.set("Select One")
        options1 = tk.OptionMenu(self, entry3, 10, 20, 30, 40)
        options1.pack()
        label5 = tk.Label(self, text="What type of investment strategy would you like to pursue?", font=("Arial", 14))
        label5.pack(pady=20, padx=20)
        entry4 = tk.StringVar(self)
        entry4.set("Select One")
        options2 = tk.OptionMenu(self, entry4, "High Reward/High Risk", "Medium Reward/Medium Risk", "Low Reward/Low Risk")
        options2.pack()
        button = ttk.Button(self, text="Submit", command=lambda: self.userInfo(entry1.get(), entry2.get(), entry3.get(), entry4.get(), controller))
        button.pack(pady=50, padx=20)

    def userInfo(self, entry1, entry2, entry3, entry4, controller):
        '''
        Stores information user has entered into a file.

        Opens user info file and writes each data item onto a different line on the file, then
        brings the InvestmentOptionsPage2 frame to the front in order to view the actual investment
        options.

        Parameters
        ----------
        entry1 : str
            User's first investment entry
        entry2 : str
            User's monthly earnings
        entry3 : str
            Percent of users monthly earnings willing to invest
        entry4 : str
            Type of investment strategy user would like
        controller : obj
            WealthifyApp object used to switch between screens.

        Returns
        -------
        None

        '''
        userInfoFile = open("Data/User_Info.txt", "w")
        userInfoFile.write(entry1+"\n")
        userInfoFile.write(entry2 + "\n")
        userInfoFile.write(entry3 + "\n")
        userInfoFile.write(entry4 + "\n")
        userInfoFile.close()
        controller.showFrame(InvestmentOptionsPage2)