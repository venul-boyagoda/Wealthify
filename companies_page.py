import tkinter as tk
from tkinter import ttk
from sub_pages import SubPages


class CompaniesPage(SubPages):
    '''
    Allows user to view or search a list of all publicly traded companies.

    User can scroll through list to see if a certain company is publicly traded or search
    a company to see if it is in the list.

    Attributes
    ----------
    None

    Methods
    -------
    sortCompanies() -> list
        Sorts list of companies.
    searchCompany()
        Searches through company list for user entry.

    '''

    def __init__(self, parent, controller):
        '''
        Initializes the CompaniesPage object.

        Uses tkinter buttons and entry to allow user to enter which company they would like to
        search and creates a listbox to view companies.

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
        label1 = tk.Label(self, text="All Publicly Traded Companies", font=("Arial", 24))
        label1.pack(pady=10, padx=20)
        label2 = tk.Label(self, text="Below is an alphabetically sorted list of all publicly traded companies.", font=("Arial", 16))
        label2.pack(pady=10, padx=20)

        list = tk.Listbox(self, selectmode=tk.MULTIPLE)
        list.insert(tk.END, *CompaniesPage.sortCompanies(self))
        list.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        label3 = tk.Label(self, text="To search for a specific company, enter the following: Company Name :  Ticker",font=("Arial", 16))
        label3.pack(pady=0, padx=20)
        entry = tk.Entry(self)
        entry.pack()
        button = ttk.Button(self, text="Search", command=lambda: CompaniesPage.searchCompany(self, entry.get(), list))
        button.pack()

    def sortCompanies(self):
        '''
        Sorts list of companies.

        Imports list of companies from file and sorts them alphabetically using pythons
        built in sort.

        Parameters
        ----------
        None

        Returns
        -------
        companiesAndTicker : list
            Sorted list of companies.

        '''
        companiesAndTickers = []
        companiesFile = open("Data/All_Publicly_Traded_Companies.txt", "r")
        for line in companiesFile:
            companiesAndTickers.append(line.rstrip("\n"))
        companiesFile.close()

        '''
        Bubble Sort:
        for i in range((len(list)) - 1):
            for a in range(0, (len(list)) - i - 1):
                if list[a] > list[a + 1]:
                    list[a], list[a + 1] = list[a + 1], list[a]
        
        Selection Sort:
        for i in range(len(list)):
            smallestElement = i
            for a in range(i + 1, len(list)):
                if list[a] < list[smallestElement]:
                    smallestElement = a
            list[i], list[smallestElement] = list[smallestElement], list[i]
        '''
        companiesAndTickers.sort()
        return companiesAndTickers

    def searchCompany(self, target, listbox):
        '''
        Searches through company list for user entry.

        Uses binary search algorithm to search through sorted list of companies for the
        users entry.

        Parameters
        ----------
        target : str
            Company user is searching for.
        listbox : obj
            Tkinter listbox where list of companies displayed.

        Returns
        -------
        None

        '''
        companyList = CompaniesPage.sortCompanies(self)
        '''
        Linear Search
        for i in range(len(list)):
            if list[i] == target:
                location = i
                found = True
        if found == False:
            location = -1
        '''

        #Bubble Search
        min = 0
        max = len(companyList) - 1
        found = False
        while min <= max and found == False:
            mid = (min + max) // 2
            if companyList[mid] == target:
                location = mid
                found = True
            elif target < companyList[mid]:
                max = mid - 1
            else:
                min = mid + 1
        if found == False:
            location = -1

        if location == -1:
            multipleLocation = []
            for i in companyList:
                if target.lower() in i.lower():
                    multipleLocation.append(companyList.index(i))
            if len(multipleLocation) > 0:
                location = -2


        if location == -1:
            label1 = tk.Label(self, text="Not in list", font=("Arial", 12))
            label1.pack()
        elif location == -2:
            for i in multipleLocation:
                companyList.insert(0, companyList.pop(i))
                listbox.delete(0,tk.END)
                listbox.insert(tk.END, *companyList)
            for i in range(len(multipleLocation)):
                listbox.select_set(i)
        else:
            listbox.see(location)
            listbox.select_set(location)