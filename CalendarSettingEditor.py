import PFC_UserBackend, json


print("Welcome!\nEnter\n1 : Customise Calendar\n2 : Load Calendar (2nd time users)")
loop=True
while (loop):
    try:
        selection = int(input("Enter: "))

        if (selection<1 or selection>2):
            print("You entered an invalid choice")

        elif (selection==1):
            print("Before we initialise your calendar, you may choose to customise certain components of your calendar")
            if (PFC_UserBackend.setYEAR()):
                while (PFC_UserBackend.UserMainSelection1()):
                    continue
            loop=False
        
        else:
            print("Before proceeding, please ensure you have the correct file name: YourCalendarSettings")
            print("Tip: You may go change the file before proceeding again without closing this application")
            loop2=True
            while (loop):
                try:
                    confirm = int(input("Enter 1 to confirm: "))

                    if (confirm==1):
                        USER_DICT = json.load(open("YourCalendarSettings.txt"))
                        PFC_UserBackend.setRETURN_DICT(USER_DICT)
                        if (PFC_UserBackend.setYEAR()):
                            while (PFC_UserBackend.UserMainSelection1()):
                                continue
                        loop2=False
                        loop=False

                except ValueError:
                    print("Error! Type 1 to confirm")

    except ValueError:
        print("Enter 1 or 2!")

json.dump(PFC_UserBackend.END(), open("YourCalendarSettings.txt", 'w'))
print("Success")