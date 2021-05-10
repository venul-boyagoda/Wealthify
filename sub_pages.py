import home_page
import tkinter as tk
from tkinter import ttk


class SubPages(tk.Frame):
    '''
    Class has certain characteristics which are common to each sub page.

    To be inherited by all sub pages as it initializes the quit and back to home buttons for a
    subpage after clicked on in the homepage.

    Attributes
    ----------
    None

    Methods
    -------
    None

    '''

    def __init__(self, parent, controller):
        '''
        Initializes the SubPage object.

        Uses tkinter buttons, along with the parent class and the controller to allow user to
        navigate to home page or quit app.

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
        button1 = ttk.Button(self, text="Back to Home Page", command=lambda: controller.showFrame(home_page.HomePage))
        button1.pack(pady=10, side="left")
        button2 = ttk.Button(self, text="Quit", command=quit)
        button2.pack(pady=10, side="right")