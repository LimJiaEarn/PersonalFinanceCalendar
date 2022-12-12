import json, datetime, calendar, openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import PatternFill, Border, Side, Alignment, Font, numbers
from openpyxl.formatting.rule import Rule, FormulaRule, CellIsRule, ColorScaleRule

# C:\Users\user\AppData\Local\Programs\Python\Python311\Scripts

#Utility lists
daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

INPUT_DICT = json.load(open("YourCalendarSettings.txt"))
YEAR = INPUT_DICT[list(INPUT_DICT)[0]]
startDayOfMonth = calendar.day_name[datetime.datetime.strptime('01 01 '+str(YEAR), '%d %m %Y').weekday() ]
startDayOfMonth_index = daysOfWeek.index(startDayOfMonth) #initially set to start day of jan(start of new year), re-used for subsequent months
#INPUT_DICT Index List
#Index 0 - YEAR
#Index 1 - CalendarDaysAndMonths
#Index 2 - START_DAY -> 0 is Monday, 6 is Sunday
#Index 3 - left_headerTitles
#Index 4 - right_headerTitles
#Index 5 - week titles

#Rows needed to offset before the first row of main data, absolute +3 because of seperator cells
rowOffset_header = max(len(INPUT_DICT[list(INPUT_DICT)[3]]), len(INPUT_DICT[list(INPUT_DICT)[4]])) +3
#Rows needed to offset in each week's block, absolute +1 because of seperator cells
rowOffset_weeks = len(INPUT_DICT[list(INPUT_DICT)[5]]) +1

#Pre-set styling colors (not user changing yet through code)
seperatorFill = PatternFill(fill_type="solid", start_color="AFB7C9")
sheetMonthFill = PatternFill(fill_type="solid", start_color="81C4E5")
sheetDaysFill = PatternFill(fill_type="solid", start_color="91D9D9")

#Create empty excel file to start working
CalendarFile = openpyxl.Workbook() 
#Delete default sheet created 
if ("Sheet1" in list(CalendarFile.get_sheet_names())):
    CalendarFile.remove_sheet(CalendarFile.sheetnames("Sheet1"))

#Utility methods

#Check if any dates exist in row
def checkRow(row):
    for i in range(2, 9):
        if (CalendarFile_currentSheet[get_column_letter(i)+str(row)].value):
            return True
    return False


#Traversing through every month and generate its content
for month in INPUT_DICT[list(INPUT_DICT)[1]].keys():
    
    #Create a sheet for each month
    CalendarFile.create_sheet(month[0:3])
    CalendarFile_currentSheet = CalendarFile[month[0:3]]
    
    #Generate styling for Header
    #Absolute referencing is used for simplicity as certain cells will not be affected by user preference
    CalendarFile_currentSheet.merge_cells("A1:H1")
    CalendarFile_currentSheet["A1"] = month.upper() + "  "+ str(YEAR)
    CalendarFile_currentSheet["A1"].font = Font(bold=True, size = 22)
    CalendarFile_currentSheet["A1"].alignment = Alignment(horizontal='center', vertical='center')
    CalendarFile_currentSheet["A1"].fill = sheetMonthFill
    CalendarFile_currentSheet.merge_cells("A2:H2")
    CalendarFile_currentSheet["A2"].fill = seperatorFill
    CalendarFile_currentSheet.merge_cells("A"+str(rowOffset_header)+":"+"H"+str(rowOffset_header))
    CalendarFile_currentSheet["A"+str(rowOffset_header)].fill = seperatorFill
    
    #Generating left header titles
    row=3
    for title, accounting in INPUT_DICT[list(INPUT_DICT)[3]].items():
        CalendarFile_currentSheet["A"+str(row)]=title
        CalendarFile_currentSheet["A"+str(row)].alignment = Alignment(horizontal='center', vertical='center')
        #This prepares the accounting row
        if (accounting==1):
            CalendarFile_currentSheet["B"+str(row)]=0
        row+=1

    #Generating right header titles
    row=3
    for title, accounting in INPUT_DICT[list(INPUT_DICT)[4]].items():
        CalendarFile_currentSheet["E"+str(row)]=title
        CalendarFile_currentSheet["E"+str(row)].alignment = Alignment(horizontal='center', vertical='center')
        #This prepares the accounting row
        if (accounting==1):
            CalendarFile_currentSheet["F"+str(row)]=0
        row+=1

    #Generating days of each week based on user preset preference
    row = rowOffset_header + 1
    start_day = INPUT_DICT[list(INPUT_DICT)[2]]
    for column in range(2, 9):
        char = get_column_letter(column)
        CalendarFile_currentSheet[char+str(row)] = daysOfWeek[start_day]
        CalendarFile_currentSheet[char+str(row)].alignment = Alignment(horizontal='center', vertical='center')
        CalendarFile_currentSheet[char+str(row)].fill = sheetDaysFill
        CalendarFile_currentSheet[char+str(row)].font = Font(bold=True, size=11)
        start_day = (start_day+1)%7
    
    #Generate dates of each week with respective to its day as set above
    date=1
    for row in range(rowOffset_header+2, rowOffset_header + rowOffset_weeks*6, rowOffset_weeks):
        for column in range(2, 9):              
            char = get_column_letter(column)
            #Ensure first date of month is inserted in the correct starting day
            if ( (date==1) and (CalendarFile_currentSheet[char+str(rowOffset_header+1)].value != startDayOfMonth) ):
                continue
            #Continuos insertion
            elif (date<=INPUT_DICT[list(INPUT_DICT)[1]][month]):   
                CalendarFile_currentSheet[char+str(row)] = date
                CalendarFile_currentSheet[char+str(row)].alignment = Alignment(horizontal='center', vertical='center')
                date+=1
            #When all dates of the month has been filled
            elif (date==INPUT_DICT[list(INPUT_DICT)[1]][month]+1): 
                startDayOfMonth = CalendarFile_currentSheet[char+str(rowOffset_header+1)].value
                date+=1 
                break
            #Simply break through remaining loops
            else:
                break

    #Generate week title for each week
    row = rowOffset_header+5
    month = month[0:3]
    CalendarFile_currentSheet = CalendarFile[month]
    while(checkRow(row)):
        for title in INPUT_DICT[list(INPUT_DICT)[5]].keys():
            CalendarFile_currentSheet["A"+str(row)]=title
            CalendarFile_currentSheet["A"+str(row)].alignment = Alignment(horizontal='center', vertical='center')
            #This prepares the accounting row
            if (INPUT_DICT[list(INPUT_DICT)[5]][title]==1):
                for i in range(2, 9):
                    CalendarFile_currentSheet[get_column_letter(i)+str(row)] = 0
            row+=1
        CalendarFile_currentSheet.merge_cells("A"+str(row)+":"+"H"+str(row))
        CalendarFile_currentSheet["A"+str(row)].fill = seperatorFill
        row+=1

    #Settng height for header portion
    CalendarFile_currentSheet.row_dimensions[1].height = 30
    for i in range(rowOffset_header):
        CalendarFile_currentSheet.row_dimensions[3+i].height = 20
        
    #Setting height for weeks layout
    row = rowOffset_header + 2
    while (CalendarFile_currentSheet["A"+str(row)].value==INPUT_DICT[list(INPUT_DICT)[5]][list(INPUT_DICT[list(INPUT_DICT)[5]])[0]]): 
        for i in range(rowOffset_weeks):
            CalendarFile_currentSheet.row_dimensions[row+i].height = 20
        row+=rowOffset_weeks
    
    #Setting width for 1st column 
    CalendarFile_currentSheet.column_dimensions["A"].width = 20
    
    #Setting width for days of week
    for i in range(2, 9):
        CalendarFile_currentSheet.column_dimensions[get_column_letter(i)].width = 25
    CalendarFile_currentSheet.row_dimensions[rowOffset_header + 1].height = 20









#Save and Exit script
CalendarFile.save("YourCalendar.xlsx")