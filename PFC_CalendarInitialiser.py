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

#Columns set as default 2 to include some aesthetics
columnOffset = 2

#Pre-set cell styling and colors (not user changing yet through code)
seperatorFill = PatternFill(fill_type="solid", start_color="AFB7C9")
sheetMonthFill = PatternFill(fill_type="solid", start_color="81C4E5")
sheetDaysFill = PatternFill(fill_type="solid", start_color="91D9D9")
headerSideFill = PatternFill(fill_type="solid", start_color="20C220")
leftheaderTitleFill = PatternFill(fill_type="solid", start_color="C5F7CA")
rightheaderTitleFill = PatternFill(fill_type="solid", start_color="F3C9DE")
weekSideFill = PatternFill(fill_type="solid", start_color="6BA4EF")
weekTitleFill = [PatternFill(fill_type="solid", start_color="C3D2F9"), PatternFill(fill_type="solid", start_color="DEF2A0"),\
                PatternFill(fill_type="solid", start_color="E0ADE9"), PatternFill(fill_type="solid", start_color="C1F6F5"),\
                PatternFill(fill_type="solid", start_color="C0BFEF"), PatternFill(fill_type="solid", start_color="EED2B8")]

thin_border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))

#Loads a user excel file, if unable to find, creates a new empty excel file
FileName = input("Enter your excel file name: ")
try:
    CalendarFile = openpyxl.load_workbook(FileName+".xlsx")
except:
    CalendarFile = openpyxl.Workbook() 

#Delete possible default sheets created
if ("Sheet1" in CalendarFile.sheetnames):
    del CalendarFile["Sheet1"]
if ("Sheet" in CalendarFile.sheetnames):
    del CalendarFile["Sheet"]
#Utility methods

#Check if any dates exist in row
def checkRow(row):
    for i in range(2, 9):
        if (CalendarFile_currentSheet[get_column_letter(columnOffset+i)+str(row)].value):
            return True
    return False

#Generate Summary Page
CalendarFile.create_sheet(str(YEAR)+" Summary")
CalendarFile_SummarySheet = CalendarFile[str(YEAR)+" Summary"]
CalendarFile_SummarySheet.merge_cells("A1:J1")
CalendarFile_SummarySheet["A1"] = str(YEAR)+" Summary"
CalendarFile_SummarySheet["A1"].font = Font(bold=True, size = 22)
CalendarFile_SummarySheet["A1"].alignment = Alignment(horizontal='center', vertical='center')
CalendarFile_SummarySheet["A1"].fill = sheetMonthFill


#Traversing through every month and generate its content
for month in INPUT_DICT[list(INPUT_DICT)[1]].keys():
    
    #Create a sheet for each month
    CalendarFile.create_sheet(month[0:3])
    CalendarFile_currentSheet = CalendarFile[month[0:3]]
    
    #Generate styling for Header
    #Absolute referencing is used for simplicity as certain cells will not be affected by user preference
    cell = get_column_letter(columnOffset)+"1"
    CalendarFile_currentSheet.merge_cells(cell+":J1")
    CalendarFile_currentSheet[cell] = month.upper() + "  "+ str(YEAR)
    CalendarFile_currentSheet[cell].font = Font(bold=True, size = 22)
    CalendarFile_currentSheet[cell].alignment = Alignment(horizontal='center', vertical='center')
    CalendarFile_currentSheet[cell].fill = sheetMonthFill
    CalendarFile_currentSheet.merge_cells(get_column_letter(columnOffset)+"2:J2")
    CalendarFile_currentSheet[get_column_letter(columnOffset)+"2"].fill = seperatorFill
    CalendarFile_currentSheet.merge_cells(get_column_letter(columnOffset)+str(rowOffset_header)+":"+"J"+str(rowOffset_header))
    CalendarFile_currentSheet[get_column_letter(columnOffset)+str(rowOffset_header)].fill = seperatorFill
    
    #Generating left header titles
    row=3
    for title, accounting in INPUT_DICT[list(INPUT_DICT)[3]].items():
        CalendarFile_currentSheet[get_column_letter(columnOffset+1)+str(row)] = title
        CalendarFile_currentSheet[get_column_letter(columnOffset+1)+str(row)].fill = leftheaderTitleFill
        for i in range(3):
            CalendarFile_currentSheet[get_column_letter(columnOffset+i)+str(row)].border = thin_border
        CalendarFile_currentSheet[get_column_letter(columnOffset+1)+str(row)].alignment = Alignment(horizontal='center', vertical='center')
        #This prepares the accounting row
        if (accounting==1):
            CalendarFile_currentSheet[get_column_letter(columnOffset+2)+str(row)]=1 #Change back to 0 eventually
        row+=1

    #Generating right header titles
    row=3
    for title, accounting in INPUT_DICT[list(INPUT_DICT)[4]].items():
        CalendarFile_currentSheet[get_column_letter(columnOffset+5)+str(row)]=title
        CalendarFile_currentSheet[get_column_letter(columnOffset+5)+str(row)].fill = rightheaderTitleFill
        for i in range(3):
            CalendarFile_currentSheet[get_column_letter(columnOffset+5+i)+str(row)].border = thin_border
        CalendarFile_currentSheet[get_column_letter(columnOffset+5)+str(row)].alignment = Alignment(horizontal='center', vertical='center')
        #This prepares the accounting row
        if (accounting==1):
            CalendarFile_currentSheet[get_column_letter(columnOffset+6)+str(row)]=1 #Change back to 0 eventually
        row+=1

    CalendarFile_currentSheet.merge_cells(get_column_letter(columnOffset)+"3"+":"+get_column_letter(columnOffset)+str(rowOffset_header-1))
    CalendarFile_currentSheet[get_column_letter(columnOffset)+"3"].fill = headerSideFill
    CalendarFile_currentSheet.column_dimensions[get_column_letter(columnOffset)].width = 2

    #Generating days of each week based on user preset preference
    row = rowOffset_header + 1
    start_day = INPUT_DICT[list(INPUT_DICT)[2]]
    for column in range(2, 9):
        char = get_column_letter(columnOffset+column)
        CalendarFile_currentSheet[char+str(row)] = daysOfWeek[start_day]
        CalendarFile_currentSheet[char+str(row)].alignment = Alignment(horizontal='center', vertical='center')
        CalendarFile_currentSheet[char+str(row)].fill = sheetDaysFill
        CalendarFile_currentSheet[char+str(row)].font = Font(bold=True, size=11)
        start_day = (start_day+1)%7
    
    #Seperator
    CalendarFile_currentSheet.merge_cells(get_column_letter(columnOffset)+str(row+1)+":"+get_column_letter(columnOffset+8)+str(row+1))
    CalendarFile_currentSheet[get_column_letter(columnOffset)+str(row+1)].fill = seperatorFill
    CalendarFile_currentSheet.row_dimensions[row+1].height = 20

    #Generate dates of each week with respective to its day as set above
    date=1
    for row in range(rowOffset_header+3, rowOffset_header + rowOffset_weeks*6, rowOffset_weeks):
        for column in range(2, 9):              
            char = get_column_letter(columnOffset+column)
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
    row = rowOffset_header+3
    weekSideFillIndex = 0
    while(checkRow(row)):
        #Aesthetic bookmarklike column
        CalendarFile_currentSheet.merge_cells(get_column_letter(columnOffset)+str(row)+":"+get_column_letter(columnOffset)+str(row+len(INPUT_DICT[list(INPUT_DICT)[5]])-1))
        CalendarFile_currentSheet[get_column_letter(columnOffset)+str(row)].fill = weekSideFill
        CalendarFile_currentSheet.column_dimensions[get_column_letter(columnOffset)].width = 2
        #Slotting titles
        for title in INPUT_DICT[list(INPUT_DICT)[5]].keys():
            CalendarFile_currentSheet[get_column_letter(columnOffset+1)+str(row)]=title
            CalendarFile_currentSheet[get_column_letter(columnOffset+1)+str(row)].fill=weekTitleFill[weekSideFillIndex%6]
            for k in range(8):
                CalendarFile_currentSheet[get_column_letter(columnOffset+1+k)+str(row)].border = thin_border
            CalendarFile_currentSheet[get_column_letter(columnOffset+1)+str(row)].alignment = Alignment(horizontal='center', vertical='center')
            #This prepares the accounting row
            if (INPUT_DICT[list(INPUT_DICT)[5]][title]==1):
                for i in range(2, 9):
                    CalendarFile_currentSheet[get_column_letter(columnOffset+i)+str(row)] = 1 #change back to 0 eventually
            row+=1
        CalendarFile_currentSheet.merge_cells(get_column_letter(columnOffset)+str(row)+":"+get_column_letter(columnOffset+8)+str(row))
        CalendarFile_currentSheet[get_column_letter(columnOffset)+str(row)].fill = seperatorFill
        row+=1
        weekSideFillIndex+=1

    #Setting height for header portion
    CalendarFile_currentSheet.row_dimensions[1].height = 30
    for i in range(rowOffset_header):
        CalendarFile_currentSheet.row_dimensions[3+i].height = 20
        
    #Setting height for weeks layout
    row = rowOffset_header + 3
    while (CalendarFile_currentSheet[get_column_letter(columnOffset+1)+str(row)].value==INPUT_DICT[list(INPUT_DICT)[5]][list(INPUT_DICT[list(INPUT_DICT)[5]])[0]]): 
        for i in range(rowOffset_weeks):
            CalendarFile_currentSheet.row_dimensions[row+i].height = 35
        row+=rowOffset_weeks
    
    #Setting width for side column 
    CalendarFile_currentSheet.column_dimensions[get_column_letter(columnOffset-1)].width = 8
    CalendarFile_currentSheet.column_dimensions[get_column_letter(columnOffset+1)].width = 20
    
    #Setting width for days of week
    for i in range(2, 9):
        CalendarFile_currentSheet.column_dimensions[get_column_letter(columnOffset+i)].width = 25
    CalendarFile_currentSheet.row_dimensions[rowOffset_header + 1].height = 20

#Save and Exit script
CalendarFile.save(FileName+".xlsx")
print(f"Calendar successfully created with filename: {FileName}!")