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

#Title, flowType, 1-header / 2-week, summation titles**
#1 - Inflow
#2 - Outflow



#For own testing
RETURN_DICT = { "YEAR": 2023,\
                "CalendarDaysAndMonths": {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31},\
                "START_DAY": 0,\
                "left_headerTitles": {"Income":1, "Investments/Dividends":1, "Comments":0},\
                "right_headerTitles": {"Rent":2, "Subscriptions":2, "Comments":0},\
                "week_titles": {"Date":0, "Notes":0, "Inflow":1,"Inflow Category":0, "Transport":2, "Meals":2, "Others":2,"Others Category":0},\
                "Overview_Inflow":[("Income", 1, 1, []), ("Miscellaneous", 1, 1, [])], \
                "Overview_Expenses":[("Rent", 2, 1, []), ("Miscellaneous", 2, 2, [])],\
                "Inflow_Breakdown":[],\
                "Expenses_Breakdown":[],\
              }


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
                            print(f"Successfully renamed from -{oldName}- to -{newName}-")
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
                            print(f"Successfully renamed from -{oldName}- to -{newName}-")
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
        AccountingRowsEditor(3)
    elif (selection2==2):
        AccountingRowsPrinter(4)
        AccountingRowsEditor(4)
    elif (selection2==3):
        AccountingRowsPrinter(5)
        AccountingRowsEditor(5)
    #This else statement should never execute
    else:
        print("Bug3!")
    return

#This function will keep looping the menu till user enters 0 to proceed
# it calls UserSelection2Direct() to enter the right sub directories
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
    print("==========\nCurrent Accounting Rows for Inflow: ")
    m=0
    for title in RETURN_DICT[list(RETURN_DICT)[dict_Index]]:
        if (title=="Date"):
            continue
        if (RETURN_DICT[list(RETURN_DICT)[dict_Index]][title]==1):
            m+=1
            print(f"{m}) {title}")
    if (m==0):
        print("NIL")
    m=0
    print("==========\nCurrent Accounting Rows for Expenses: ")
    for title in RETURN_DICT[list(RETURN_DICT)[dict_Index]]:
        if (title=="Date"):
            continue
        if (RETURN_DICT[list(RETURN_DICT)[dict_Index]][title]==2):
            m+=1
            print(f"{m}) {title}")
    if (m==0):
        print("NIL")
    m=0
    print("==========\nCurrent Rows not set: ")
    for title in RETURN_DICT[list(RETURN_DICT)[dict_Index]]:
        if (title=="Date"):
            continue
        if (RETURN_DICT[list(RETURN_DICT)[dict_Index]][title]==0):
            m+=1
            print(f"{m}) {title}")    
    if (m==0):
        print("NIL")
    print("==========")

def AccountingRowsEditor2(dict_Index, choice):
    loop=True
    while (loop):
        title = input("Enter title name: ")
        if ((title not in RETURN_DICT[list(RETURN_DICT)[dict_Index]]) or (title=="Date")):
            print("Invalid title!")
        else:
            RETURN_DICT[list(RETURN_DICT)[dict_Index]][title] = choice%3
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

def BreakdownRowsInitialise():
    for di in range(3, 5): #Headers
        for title in RETURN_DICT[list(RETURN_DICT)[di]]:
            if (RETURN_DICT[list(RETURN_DICT)[di]][title]==1):
                RETURN_DICT[list(RETURN_DICT)[8]].append([title, 1, 1, []])
                
            elif (RETURN_DICT[list(RETURN_DICT)[di]][title]==2):
                RETURN_DICT[list(RETURN_DICT)[9]].append([title, 2, 1, []]) 
    for di in range(5, 6): #Weeks
        for title in RETURN_DICT[list(RETURN_DICT)[di]]:
            if (RETURN_DICT[list(RETURN_DICT)[di]][title]==1):
                RETURN_DICT[list(RETURN_DICT)[8]].append([title, 1, 2, []])
                
            elif (RETURN_DICT[list(RETURN_DICT)[di]][title]==2):
                RETURN_DICT[list(RETURN_DICT)[9]].append([title, 2, 2, []]) 

##========================================================================================================================#

#This function is called by UserMainSelection3() to direct users to their respective functions
def UserSelection3Direct(selection3):
    #Set Start Day of week
    if (selection3==1):
        OverviewRowsEditor(6)
    elif (selection3==2):
        OverviewRowsEditor(7)
    elif (selection3==3):
         OverviewRowsEditor(8)
    #Edit Weekly Rows
    elif (selection3==4):
         OverviewRowsEditor(9)
    #This else statement should never execute
    else:
        print("Bug4!")
    return

#This function will keep looping the menu till user enters 0 to proceed, it calls UserSelection3Direct() to enter the right sub directories
#
def UserMainSelection3():
    print("Now you may choose to customise a yearly overview page\nNote: Overview is empty by default, Breakdown contains all accounting rows by default")
    while True:
        print("Enter a selection below:")
        print("1 : Edit Inflow Overview rows") #index 6
        print("2 : Edit Expenses Overview rows") #index 7
        print("3 : Edit Inflow breakdown rows") #index 8
        print("4 : Edit Expenses breakdown rows") #index 9
        print("5 : Display current Inflow and Expenses row titles")
        print("0 : Proceed !")
        loop=True
        while (loop):
            try:
                selection3 = int(input("Selection: "))
                if (selection3<0 or selection3 > 5):
                    print("Invalid selection!")
                else:
                    if (selection3==0):
                        return False
                    elif (selection3==5):
                        InflowOutflowRowsPrinter(1) #prints all inflow row
                        InflowOutflowRowsPrinter(2) #prints all expenses row
                        loop=False
                    else:
                        UserSelection3Direct(selection3)
                        loop=False
            except ValueError:
                print("Invalid selection! Use numbers")

#
def InflowOutflowRowsPrinter(flowType):
    if (flowType==1):
        print("==========\nList of rows for Inflow: ")
    else:
        print("==========\nList of rows for Expenses: ")
    m=0
    for di in range(3, 6):
        for title in RETURN_DICT[list(RETURN_DICT)[di]]:
            if (RETURN_DICT[list(RETURN_DICT)[di]][title]==flowType):

                m+=1
                print(f"{m}) {title}")
    if (m==0):
        print("NIL")
    print("==========")

#
def checkAccounting(titleTC, acctVal):
    for di in range(3, 6):
        for title in RETURN_DICT[list(RETURN_DICT)[di]]:
            
            if (title==titleTC and RETURN_DICT[list(RETURN_DICT)[di]][titleTC]==acctVal):
                return True
    return False

#If no more valid accounting rows can be added, let the user know
#
def checkMaxARows(dict_Index):
    num=0
    for di in range(3, 6):
        for title in RETURN_DICT[list(RETURN_DICT)[di]]:
            if (RETURN_DICT[list(RETURN_DICT)[di]][title]==(dict_Index%2)+1):
                num+=1
    if (num==len(RETURN_DICT[list(RETURN_DICT)[dict_Index]])):
        return True
    return False

def checkHeaderWeekbyUser(title, hw):

    #Checking for user
    if (hw==1):
        for di in range(3, 5):
            if title in RETURN_DICT[list(RETURN_DICT)[di]]:
                return hw
        print("The title you chose is not from the header list!")
        return 0

    else:
        if title in RETURN_DICT[list(RETURN_DICT)[5]]:
            return hw
        print("The title you chose is not from the week list!")
        return 0

#Same as above function, except it returns the flowType
def getflowTypeAfterHeaderWeekByUser(title, hw):
    #Checking for user
    if (hw==1):
        for di in range(3, 5):
            if title in RETURN_DICT[list(RETURN_DICT)[di]]:
                return RETURN_DICT[list(RETURN_DICT)[di]][title]
        print("The title you chose is not from the header list!")
        return 0

    else:
        if title in RETURN_DICT[list(RETURN_DICT)[5]]:
            return RETURN_DICT[list(RETURN_DICT)[5]][title]
        print("The title you chose is not from the week list!")
        return 0



def OverviewRowsEditor2(dict_Index, choice, flowType): 
    #choice=1 -> Add
    #choice=2 -> Remove
    if (choice<3):
        loop=True
        while (loop):
            title = input("Enter title name: ")
            if (not(checkAccounting(title, flowType))):
                print("Invalid title!")
                loop=False
            else:
                if (choice==1):

                    doubleC=1
                    for tup in RETURN_DICT[list(RETURN_DICT)[dict_Index]]:
                        if (tup[0]==title):
                            print("Repeated title! Title is already in list")
                            loop=False
                            doubleC=0
                    if (doubleC==1):
                        loop2=True
                        while(loop2):
                            try:    
                                hw = int(input("Enter 1 if your title is from headers and 2 if your title is from week: "))
                                if (hw==1 or hw==2):
                                    if(checkHeaderWeekbyUser(title, hw)!=0): #Checks for correctness
                                        RETURN_DICT[list(RETURN_DICT)[dict_Index]].append([title, (dict_Index%2)+1, hw, []])
                                        loop=False
                                        loop2=False
                                        print("Successfully added!")
                                    else:
                                        loop2=False
                                else:
                                    print("You entered an invalid number!")
                            except ValueError:
                                print("You entered an invalid number!")

                         
                else:
                    ch=0
                    for tup in RETURN_DICT[list(RETURN_DICT)[dict_Index]]:
                        if (tup[0]==title):
                            RETURN_DICT[list(RETURN_DICT)[dict_Index]].remove(tup)
                            print("Successfully removed!")
                            loop=False
                            ch=1
                    if (ch==0):
                        print("Unable to find title you requested to remove")
                        loop=False

    #choice=4 -> Summation rows
    else:

        #Given flowType already
        sumRowTitle = input("Enter your Summation Row name: ")
        if (flowType==1):
            print("Note: You can only choose Inflow titles")
        else:
            print("Note: You can only choose Outflow rows")

        #Adds sumRowTitle entry into dict_Index of lists, with an empty summation row to be filled
        #hw set to 0 as not used for summation rows
        RETURN_DICT[list(RETURN_DICT)[dict_Index]].append([sumRowTitle, flowType, 0, []])

        check = [] #temp array to check no repeated titles are added, will be initialised to RETURN_DICT at final step
        loop=True
        while (loop):
            print("Enter name of titles you want to add in summmation rows: ")

            if (len(check)!=0):
                print("Current titles your summation rows: ")
                count=1
                for tup in check:
                    print(f"{count}) {tup[0]}")
                    count+=1
            print() #Print empty line for better visual

            print("Enter EXIT if you have no more titles to add")
            sumRowAdd = input("Title: ")        

            if (sumRowAdd != "EXIT"):
                loop2=True
                while(loop2):
                    try:    
                        hw = int(input("Enter 1 if your title is from headers and 2 if your title is from week: "))
                        if (hw==1 or hw==2):

                            if(checkHeaderWeekbyUser(sumRowAdd, hw)!=0 and getflowTypeAfterHeaderWeekByUser(sumRowAdd, hw)==flowType): #Checks for correctness
                                
                                if ((sumRowAdd, hw) not in check): #Checks for duplicate
                                    check.append((sumRowAdd, hw))
                                else:
                                    print("Title has been added previously!")
                                loop2=False

                            elif (checkHeaderWeekbyUser(sumRowAdd, hw)==0):
                                if (hw==1):
                                    print("We could not find your title in headers")
                                else:
                                    print("We could not find your title in weeks")
                                loop2=False #This makes user enter both title and header/week index again
                            elif (getflowTypeAfterHeaderWeekByUser(sumRowAdd, hw)!=flowType):
                                print("You entered a title of the wrong flow type")
                                loop2=False
                        else:
                            print("You entered an invalid number!")
                    except ValueError:
                        print("You entered an invalid number!")

            else:
                loop=False

        #Update check to list, current instance summation row is always the last one
        RETURN_DICT[list(RETURN_DICT)[dict_Index]][len(RETURN_DICT[list(RETURN_DICT)[dict_Index]])-1][3] = check

        print("Successfully added Summation row: "+ sumRowTitle)
        print("This is immutable, however you may choose to remove this row and edit again")

    return

def reOrder2(reOrderList, startIndex):
    temp_list=[]
    check = [] #To check and ensure user do not enter repeated indexes
    
    length = len(reOrderList)
    for i in range(startIndex, length):
        print(f"Index {i+1}: {reOrderList[i][0]}")
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
        temp_list.append(reOrderList[index])
    reOrderList.clear()
    reOrderList = temp_list
    print("Successfully re-ordered!")
    
    return reOrderList




def OverviewRowsEditor(dict_Index):
    loop=True
    while(loop):
        print("Current titles:")
        m=0
        for title in RETURN_DICT[list(RETURN_DICT)[dict_Index]]:
            m+=1
            print(f"{m}) {title[0]}")
        if (m==0):                
            print("NIL")

        print("Enter a selection below")
        print("1 : Add row")
        print("2 : Remove row")
        print("3 : Re-order row")
        print("4 : Add Summation row *")
        print("0 : Exit")
        try:
            choice = int(input("Selection: "))

            if (choice==1 and checkMaxARows(dict_Index)):
                if ((dict_Index%2)+1):
                    print("You have added all possible Inflow rows")
                else:
                    print("You have added all possible Expense rows")
                
            elif (choice<0 or choice > 4):
                print("Invalid selection!")
            else:
                if (choice==0):
                    return
                elif (choice==3):  
                    RETURN_DICT[list(RETURN_DICT)[dict_Index]] = reOrder2(RETURN_DICT[list(RETURN_DICT)[dict_Index]], 0)
                else:
                    OverviewRowsEditor2(dict_Index, choice, (dict_Index%2)+1)
        except ValueError:
            print("Invalid selection! Use numbers")