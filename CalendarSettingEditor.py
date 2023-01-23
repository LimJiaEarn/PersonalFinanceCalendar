import PFC_UserBackend, json


print("Welcome!\nEnter\n1 : Customise Calendar from default\n2 : Load previous Calendar settings (2nd time users)")
loop=True
while (loop):
    try:
        selection = int(input("Enter: "))

        if (selection<1 or selection>2):
            print("You entered an invalid choice")

        elif (selection==1):
            print("Before we initialise your calendar, you may choose to customise certain components of your calendar")
            if (PFC_UserBackend.setYEAR()):
                while (PFC_UserBackend.UserMainSelection1()): #Sets monthly page
                    continue
                while (PFC_UserBackend.UserMainSelection2()): #Sets accounting rows 
                    continue  
                PFC_UserBackend.BreakdownRowsInitialise() #Initialise breakdown rows for overview page
                while (PFC_UserBackend.UserMainSelection3()): #Sets year overview page
                    continue 



            loop=False
        
        else:
            print("Feature still under construction!\nRedirecting you to customise calendar from default")
            PFC_UserBackend.setYEAR()
            loop=False
            print("debug")
            
            # print("Before proceeding, please ensure you have the correct file name: YourCalendarSettings")
            # print("Tip: You may go change the file before proceeding again without closing this application")
            # loop2=True
            # while (loop):
            #     try:
            #         confirm = int(input("Enter 1 to confirm: "))

            #         if (confirm==1):
            #             USER_DICT = json.load(open("YourCalendarSettings.txt"))
            #             PFC_UserBackend.setRETURN_DICT(USER_DICT)
            #             if (PFC_UserBackend.setYEAR()):
            #                 while (PFC_UserBackend.UserMainSelection1()):
            #                     continue
            #             loop2=False
            #             loop=False

            #     except ValueError:
            #         print("Error! Type 1 to confirm")

    except ValueError:
        print("Enter 1 or 2!")


json.dump(PFC_UserBackend.END(), open("YourCalendarSettings.txt", 'w'))
print("Your settings have been saved in the text file - YourCalendarSettings\nYou may re-use this setting again for future calendars or edit from this again by choosing to Load Calendar in the future")

print("Enter\n1 : Initialise Calendar now\n2 : Exit")
while True:
    try:
        selection = int(input("Enter: "))
        if (selection<1 or selection>2):
            print("You entered an invalid number!")
        elif (selection==1):
            exec(open("PFC_CalendarInitialiser.py").read())
            break
        else:
            break

    except ValueError:
        print("Invalid input!")


print("Exiting Application...")