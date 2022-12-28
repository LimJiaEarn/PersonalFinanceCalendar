# Contains all python code for UI
#These are the default titles, there will be no change to this
left_headerTitles_original = {"Income":1, "Investments/Dividends":1, "Comments":0}
right_headerTitles_original = {"Rent":1, "Subscriptions":1, "Comments":0}
week_titles_original = {"Date":0, "Notes":0, "Inflow":0,"Inflow Category":0, "Expenses":1, "Expenses Category":0}
Overview_Inflow_original = ["Income", "Others"]
Overview_Outflow_original = ["Rent", "Services", "Others"]

#This dictionary stores everything we need to initialise the calendar where its value will be initialised systematically by default or by user
#It is initialised with default values
#Index 0 - YEAR
#Index 1 - CalendarDaysAndMonths
#Index 2 - START_DAY -> 0 is Monday, 6 is Sunday
#Index 3 - left_headerTitles
#Index 4 - right_headerTitles
#Index 5 - week titles
#Index 6 - Main Inflow Overview
#Index 7 - Main Expenses Overview 
#Index 8 - Inflow Breakdown
#Index 9 - Outflow Breakdown


#1 - Inflow
#2 - Outflow

# RETURN_DICT = { "YEAR": 2023,\
#                 "CalendarDaysAndMonths": {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31},\
#                 "START_DAY": 0,\
#                 "left_headerTitles": {"Income":1, "Investments/Dividends":1, "Comments":0},\
#                 "right_headerTitles": {"Rent":1, "Subscriptions":1, "Comments":0}, \
#                 "week_titles": {"Date":0, "Notes":0, "Inflow":0,"Inflow Category":0, "Miscellaneous":1, "Miscellaneous Category":0},\
#                 "Overview_Inflow":["Income", "Others"],
#                 "Overview_Expenses":["Rent", "Services", "Others"]}

#For own testing
RETURN_DICT = { "YEAR": 2023,\
                "CalendarDaysAndMonths": {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31},\
                "START_DAY": 0,\
                "left_headerTitles": {"Income":1, "Investments/Dividends":1, "Comments":0},\
                "right_headerTitles": {"Rent":2, "Subscriptions":2, "Comments":0},\
                "week_titles": {"Date":0, "Notes":0, "Inflow":1,"Inflow Category":0, "Transport":2, "Meals":2, "Others":2,"Others Category":0},\
                "Overview_Inflow":["Income", "Miscellaneous"], \
                "Overview_Expenses":["Rent", "Transport", "Meals", "Miscellaneous"] }


#For debugging
def printRETURN_DICT():
    print("=====Debugging: Check DICT=====")
    for key, value in RETURN_DICT.items():
        print(f"key: {key}, value: {value}")

    print("===============================")
    return

#Last function call
def END():
    return RETURN_DICT


def setRETURN_DICT(User_Dictionary):
    RETURN_DICT = User_Dictionary

def setYEAR():
    while True:
        try:
            YEAR = int(input("Enter year of calendar: "))
            if (YEAR<2022 or YEAR>2100):
                print("Invalid year!")
            else:
                #If leap year, days in Feb changed to 29 else
                if ( (YEAR % 400 == 0) or (YEAR % 100 != 0) and (YEAR % 4 == 0) ):     
                    updateRETURN_DICT(1, 29)

                updateRETURN_DICT(0, YEAR)
                return True

        except ValueError:
            print("Invalid year! Use numbers")  

def updateRETURN_DICT(keyIndex, newValue):

    if (keyIndex==0):
        RETURN_DICT[list(RETURN_DICT)[keyIndex]] = newValue

    #We only edit index 1 for leap years so newValue passed in is the new Feb days only
    elif (keyIndex==1):
        RETURN_DICT[list(RETURN_DICT)[keyIndex]]["February"] = newValue
    
    elif (keyIndex==2):
        RETURN_DICT[list(RETURN_DICT)[keyIndex]] = newValue



    else:
        print("Bug1!")


    return


#This function is called by UserMainSelection1() to direct users to their respective functions
def UserSelection1Direct(selection1):
    #Set Start Day of week
    if (selection1==1):
        setSTART_DAY()
    elif (selection1==2):
        EditHeaderTitles(3)
    
    elif (selection1==3):
        EditHeaderTitles(4)
    #Edit Weekly Rows
    elif (selection1==4):
        EditWeekTitles()
    #This else statement should never execute
    else:
        print("Bug2!")
    return


#This function will keep looping the menu till user enters 0 to proceed, it calls UserSelection1Direct() to enter the right sub directories
def UserMainSelection1():
    while True:
        print("Enter a selection below:")
        print("1 : Choose preference for start day of week")
        print("2 : Edit Left Header")
        print("3 : Edit Right Header")
        print("4 : Edit Weekly Rows")
        print("0 : Proceed !")
        loop=True
        while (loop):
            try:
                selection1 = int(input("Selection: "))
                if (selection1<0 or selection1 > 4):
                    print("Invalid selection!")
                else:
                    if (selection1==0):

                        return False
                    else:
                        UserSelection1Direct(selection1)
                        loop=False

            except ValueError:
                print("Invalid selection! Use numbers")


def setSTART_DAY():
    print("Choose your preference on which day you prefer your calendar to start:\nBy default start day is set as Monday")
    while True:
        try:
            start_day = int(input("1. Monday\n2. Tuesday\n3. Wednesday\n4. Thursday\n5. Friday\n6. Saturday\n7. Sunday\n"))
            if (start_day<1 or start_day>7):
                print("Invalid preference! Choose between 1 and 7")
            else:
                updateRETURN_DICT(2, start_day-1)
                print("Successfully set!")
                return
        except ValueError:
            print("Enter a valid preference! (e.g: 1, 2..7)")


def EditWeekTitles():
    while True:
        print("Current week titles")
        for i in range(0, len(RETURN_DICT[list(RETURN_DICT)[5]])):
            print(f"{i+1}: {list(RETURN_DICT[list(RETURN_DICT)[5]])[i]}" )
        print("Enter\n1 - Add title\n2 - Remove title\n3 - Rename title\n4 - Re-order titles\n5 - Revert to default week titles\n0 - Save and exit")
        try:
            
            choice = int(input("Selection: "))

            if (choice<0 or choice>5):
                print("Error!")
            
            #Adding week titles
            elif (choice==1):
                while True:
                    newWeekTitle = input("Enter your new title here: ")
                    if (newWeekTitle in RETURN_DICT[list(RETURN_DICT)[5]] ):
                        print("Title already exist!")
                    else:
                        RETURN_DICT[list(RETURN_DICT)[5]][newWeekTitle] = 0 #Accounting value set to 0 as default
                        print("Successfully added title!")
                        break
            
            #Removing week titles
            elif (choice==2):
                print("NOTE: You are not allowed to remove Date")
                print("Current week titles")
                for i in range(1, len(RETURN_DICT[list(RETURN_DICT)[5]])):
                    print(f"Index {i}: {list(RETURN_DICT[list(RETURN_DICT)[5]])[i]}" )
                    
                print("Enter index of week title to remove: ")
                loop=True
                while (loop):
                    try:
                        index=int(input("Index: "))
                        if (index<1 or index>len(RETURN_DICT[list(RETURN_DICT)[5]])-1):
                            print("You entered an invalid index")
                        else:
                            del RETURN_DICT[list(RETURN_DICT)[5]][list(RETURN_DICT[list(RETURN_DICT)[5]])[index]]
                            print("Successfully removed title!")
                            loop=False
                        
                    except ValueError:
                        print("Invalid index, it should be a number!")
                    
            
            #Rename week titles
            elif (choice==3):
                print("Current week titles")
                for i in range(1, len(RETURN_DICT[list(RETURN_DICT)[5]])):
                    print(f"Index {i}: {list(RETURN_DICT[list(RETURN_DICT)[5]])[i]}" )

                print("Enter index of week title to rename: ")
                loop=True
                while (loop):
                    try:
                        index=int(input("Index: "))
                        if (index<1 or index>len(RETURN_DICT[list(RETURN_DICT)[5]])-1):
                            print("You entered an invalid index")
                        else:
                            oldName=list(RETURN_DICT[list(RETURN_DICT)[5]])[index]  
                            newName = input("New week title name: ")
                            temp_dict={}
                            for key in RETURN_DICT[list(RETURN_DICT)[5]].keys():
                                if (key != oldName):
                                    temp_dict[key]=RETURN_DICT[list(RETURN_DICT)[5]][key]
                                else:
                                    temp_dict[newName]=RETURN_DICT[list(RETURN_DICT)[5]][oldName]
                            RETURN_DICT[list(RETURN_DICT)[5]] = temp_dict
                            if (oldName=="Expenses"):
                                RETURN_DICT[list(RETURN_DICT)[5]][newName] = 0
                            print(f"Successfully renamed from {oldName} to {newName}")
                            loop=False

                    except ValueError:
                        print("Invalid index, it should be a number!")
            
            #Reorder week titles
            elif (choice==4):
                print("NOTE: You are not allowed to re-order Date")
                RETURN_DICT[list(RETURN_DICT)[5]] = reOrder(RETURN_DICT[list(RETURN_DICT)[5]], 1)

            #Revert to default week titles
            elif (choice==5):
                RETURN_DICT[list(RETURN_DICT)[5]] = week_titles_original
                print("Successfully reverted!")
                
            #Exit
            else:
                return

        except ValueError:
            print("Error!")

def reOrder(Dictionary, startIndex):
    temp_dictionary={}
    check = [] #To check and ensure user do not enter repeated indexes
    
    length = len(Dictionary)
    for i in range(startIndex, length):
        print(f"Index {i+1}: {list(Dictionary)[i]}")
    if(startIndex!=0): #This if block only applies for week headers
        temp_dictionary[list(Dictionary)[0]] = Dictionary[list(Dictionary)[0]]
    print("Enter the new order from left to right by the current index")
    print("E.g: 3 2 1 will reverse the order")
    print("Note: Enter one index at a time, you will be prompted as may times as no. of indexes")
    for i in range(startIndex, length):
        while True:
            try:
                index=int(input("New Index: "))
            except ValueError:
                print("Invalid index, it should be a number!")

            if ((index<1+startIndex) or (index > length)):
                print("You entered an invalid index")
            elif (index in check):
                print("You entered a repeated index")
            else:
                check.append(index)
                index-=1
                break       
        temp_dictionary[list(Dictionary)[index]] = Dictionary[list(Dictionary)[index]]
    Dictionary.clear()
    Dictionary = temp_dictionary
    print("Successfully re-ordered!")
    
    return Dictionary

def EditHeaderTitles(dictIndex):
    while True:
        print("Current header titles")
        for i in range(len(RETURN_DICT[list(RETURN_DICT)[dictIndex]])):
            print(f"{i+1}: {list(RETURN_DICT[list(RETURN_DICT)[dictIndex]])[i]}")
        print("Enter\n1 - Add title\n2 - Remove title\n3 - Rename titles\n4 - Re-order titles\n5 - Revert to default headers\n0 - Save and exit")
        try:
            choice = int(input("Enter: "))
            #Check for valid choice number
            if (choice<0 or choice>5):
                print("Error!")
                continue
            
            #Adding header titles
            elif (choice==1):
                while True:
                    newHeaderTitle = input("Enter your new title here: ")
                    if (newHeaderTitle in RETURN_DICT[list(RETURN_DICT)[dictIndex]] ):
                        print("Title already exist!")
                    else:
                        RETURN_DICT[list(RETURN_DICT)[dictIndex]][newHeaderTitle] = 0 #Accounting value set to 0 as default
                        print("Successfully added title!")
                        break
            
            #Removing header titles
            elif (choice==2):
                print("Current header titles")
                for i in range(len(RETURN_DICT[list(RETURN_DICT)[dictIndex]])):
                    print(f"Index {i+1}: {list(RETURN_DICT[list(RETURN_DICT)[dictIndex]])[i]}")
                print("Enter index of header title to remove: ")
                loop=True
                while (loop):
                    try:
                        index=int(input("Index: "))
                        index-=1
                        if (index<0 or index>len(RETURN_DICT[list(RETURN_DICT)[dictIndex]])-1):
                            print("You entered an invalid index")
                        else:
                            del RETURN_DICT[list(RETURN_DICT)[dictIndex]][list(RETURN_DICT[list(RETURN_DICT)[dictIndex]])[index]]
                            print("Successfully removed title!")
                            loop=False

                    except ValueError:
                        print("Invalid index, it should be a number!")

                
            #Renaming header titles
            elif (choice==3):
                print("Current header titles")
                for i in range(len(RETURN_DICT[list(RETURN_DICT)[dictIndex]])):
                    print(f"Index {i+1}: {list(RETURN_DICT[list(RETURN_DICT)[dictIndex]])[i]}")
                print("Enter index of header title to rename: ")
                loop=True
                while (loop):
                    try:
                        index=int(input("Index: "))
                        index-=1
                        if (index<0 or index>len(RETURN_DICT[list(RETURN_DICT)[dictIndex]])-1):
                            print("You entered an invalid index")
                        else:
                            oldName=list(RETURN_DICT[list(RETURN_DICT)[dictIndex]])[index]   
                            newName = input("New header title name: ")
                            temp_dict={}
                            for key in RETURN_DICT[list(RETURN_DICT)[dictIndex]].keys():
                                if (key != oldName):
                                    temp_dict[key]=RETURN_DICT[list(RETURN_DICT)[dictIndex]][key]
                                else:
                                    temp_dict[newName]=RETURN_DICT[list(RETURN_DICT)[dictIndex]][oldName]
                            RETURN_DICT[list(RETURN_DICT)[dictIndex]] = temp_dict
                            print(f"Successfully renamed from {oldName} to {newName}")
                            loop=False
                    except ValueError:
                        print("Invalid index, it should be a number!")
                    
                
            #Reordering header titles
            elif (choice==4):  
                RETURN_DICT[list(RETURN_DICT)[dictIndex]] = reOrder(RETURN_DICT[list(RETURN_DICT)[dictIndex]], 0)

            #Reverting header titles back to default
            elif (choice==5):
                if (dictIndex==3):
                    RETURN_DICT[list(RETURN_DICT)[dictIndex]] = left_headerTitles_original
                else:
                    RETURN_DICT[list(RETURN_DICT)[dictIndex+1]] = right_headerTitles_original
                print("Successfully reverted!")
            
            #Exit
            else:
                return

        except ValueError:
            print("Error!")

##========================================================================================================================#

#This function is called by UserMainSelection2() to direct users to their respective functions
def UserSelection2Direct(selection2):

    if (selection2==1):
        AccountingRowsPrinter(3)
    elif (selection2==2):
        AccountingRowsPrinter(4)
    elif (selection2==3):
        AccountingRowsPrinter(5)
    #This else statement should never execute
    else:
        print("Bug3!")
    return

#This function will keep looping the menu till user enters 0 to proceed, it calls UserSelection2Direct() to enter the right sub directories
def UserMainSelection2():
    print("Now you may choose rows for inflows and expenses to generate an accurate summary page")
    while True:
        print("Enter a selection below:")
        print("1 : Edit Left header accounting rows")
        print("2 : Edit Right header accounting rows")
        print("3 : Edit weekly accounting rows")
        print("0 : Proceed !")
        loop=True
        while (loop):
            try:
                selection2 = int(input("Selection: "))
                if (selection2<0 or selection2 > 3):
                    print("Invalid selection!")
                else:
                    if (selection2==0):

                        return False
                    else:
                        UserSelection2Direct(selection2)
                        loop=False
            except ValueError:
                print("Invalid selection! Use numbers")

def AccountingRowsPrinter(dict_Index):
    print("==========\nCurrent Accounting Rows for inflow: ")
    m=0
    for title in RETURN_DICT[list(RETURN_DICT)[dict_Index]]:
        if (RETURN_DICT[list(RETURN_DICT)[dict_Index]][title]==1):
            m+=1
            print(f"{m}) {title}")
    if (m==0):
        print("NIL")
    m=0
    print("==========\nCurrent Accounting Rows for expenses: ")
    for title in RETURN_DICT[list(RETURN_DICT)[dict_Index]]:
        if (RETURN_DICT[list(RETURN_DICT)[dict_Index]][title]==2):
            m+=1
            print(f"{m}) {title}")
    if (m==0):
        print("NIL")
    m=0
    print("==========\nCurrent Rows not set: ")
    for title in RETURN_DICT[list(RETURN_DICT)[dict_Index]]:
        if (RETURN_DICT[list(RETURN_DICT)[dict_Index]][title]==0):
            m+=1
            print(f"{m}) {title}")    
    if (m==0):
        print("NIL")
    print("==========")

def AccountingRowsEditor2(dict_Index, choice):
    #Choice=1 -> Add row to inflow
    #Choice=2 -> Add row to outflow
    #Choice=3 -> Remove row from accounting
    loop=True
    while (loop):
        title = input("Enter title name: ")
        if (title not in INPUT_DICT[list(INPUT_DICT)[dict_Index]]):
            print("Invalid title!")
        else:
            INPUT_DICT[list(INPUT_DICT)[dict_Index]][title] = choice%3
            loop=False
                
    return
    
def AccountingRowsEditor(dict_Index):
    loop=True
    while(loop):
        AccountingRowsPrinter(dict_Index)
        print("Enter a selection below")
        print("1 : Add row to Inflow")
        print("2 : Add row to Expenses")
        print("3 : Exclude row from accounting")
        print("0 : Exit")
        try:
                choice = int(input("Selection: "))
                if (choice<0 or choice > 3):
                    print("Invalid selection!")
                else:
                    if (choice==0):
                        loop = False
                    else:
                        AccountingRowsEditor2(dict_Index, choice)
                        print("Success!")
        except ValueError:
            print("Invalid selection! Use numbers")



##========================================================================================================================#



#This function is called by UserMainSelection2() to direct users to their respective functions
def UserSelection3Direct(selection3):
    #Set Start Day of week
    if (selection3==1):
        addInflowOverviewRows()
    elif (selection3==2):
        addExpensesOverviewRows()
    
    elif (selection3==3):
        addInflowBreakdownRows()
    #Edit Weekly Rows
    elif (selection3==4):
        addExpensesBreakdownRows()
    #This else statement should never execute
    else:
        print("Bug4!")
    return

#This function will keep looping the menu till user enters 0 to proceed, it calls UserSelection3Direct() to enter the right sub directories
def UserMainSelection3():
    print("Now you may choose to customise a yearly overview page\nNote: Overview is empty by default, Breakdown contains all accounting rows by default")
    while True:
        print("Enter a selection below:")
        print("1 : Add Inflow Overview rows")
        print("2 : Add Expenses Overview rows")
        print("3 : Add Inflow breakdown rows")
        print("4 : Add Expenses breakdown rowss")
        print("0 : Proceed !")
        loop=True
        while (loop):
            try:
                selection3 = int(input("Selection: "))
                if (selection3<0 or selection3 > 4):
                    print("Invalid selection!")
                else:
                    if (selection3==0):

                        return False
                    else:
                        UserSelection2Direct(selection3)
                        loop=False
            except ValueError:
                print("Invalid selection! Use numbers")



def addInflowOverviewRows():
    print("TBC")

def addExpensesOverviewRows():
    print("TBC")


def addInflowBreakdownRows():
    print("TBC")


def addExpensesBreakdownRows():
    print("TBC")