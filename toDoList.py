import os, time

allList = []
high = []
medium = []
low = []

def addList():

    while True:

        row = [input("What is the task? > ").lower().strip(), input("When is it due by? > ").lower().strip(), input("What is the priority? > ").lower().strip()]
        allList.append(row)

        if row[2] == "high":
            high.append(row)

        elif row[2] == "medium":
            medium.append(row)

        elif row[2] == "low":
            low.append(row)

        else:
            print("\nBAD INPUT!\n")
            continue
        
        print("\nHere are your tasks: ")
        print(allList)
        
        again = input("\nDo you want to continue? (y/n) ").lower().strip()
        print()

        if again[0] == "n":
            break
        else:
            continue

def viewList():

    if len(allList) == 0:

            print("\nYour list is empty!")
            print("Please, add tasks first\n")
        
    else:
        whatView = input("\nview all or view priority? \n").lower().strip()

        if whatView == "view all":

            print("\nHere is your List: ")
            print(allList)
    
        elif whatView == "view priority":

            print("\nHere is your 'HIGH' priority List: ")
            print(high)
            print("\n")
            print("\nHere is your 'MEDIUM' priority List: ")
            print(medium)
            print("\n")
            print("\nHere is your 'LOW' priority List: ")
            print(low)
            print("\n")

def delItem():

    if len(allList) == 0:

            print("\nYour list is empty!")
            print("Please, add tasks first\n")
        
    else:

        delWhat = input("\nWhat item do you want to delete? >> ").lower().strip()
        for row in allList:
            if delWhat in row:
                allList.remove(row)

        print("\nHere is your updated list: ")
        print(allList)

def editItem():
    
    if len(allList) == 0:

            print("\nYour list is empty!")
            print("Please, add tasks first\n")
        
    else:

        print("\nHere is your tasks: ")
        print(allList)
        print()

        editWhat = input("\nWhat task do you want to edit? >> ")
        for row in allList:
            if editWhat in row:
                newTask = input("\nwhat is the new task? >> ")
                position = row.index(editWhat)
                row[position] = newTask
        print("\nHere is the updated list: ")
        print(allList)
        print()

while True:

    userAction = input("\nDo you want to add, view, edit or remove a to do or exit? > ").lower().strip()
    print()

    if userAction[0] == "a":
        addList()

    elif userAction[0] == "v":
        viewList()

    elif userAction[0] == "r" or userAction[0] == "d":
        delItem()
    
    elif userAction == "edit":
        editItem()
    
    elif userAction == "exit" or userAction[0] == "q":
        if userAction != "quit" or userAction == "quit":
            print("\nI know that you want to go out")
            print("Keep safe!\n")
            time.sleep(1)
            break
    else:
        print("\nSorry, bad input!")
    
print("\n\nGoodBYE")
time.sleep(2)
exit()