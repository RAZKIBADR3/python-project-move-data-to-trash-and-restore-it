import os
print("\t\t\t\t\t\twelcome to our application")

def EnterData(data):
    data.append(input("enter the name of personne\n"))
    Q = input("do you want continue yes or no 'enter y or n'\n")
    while Q=="y" :
        data.append(input("enter the name of personne\n"))
        Q = input("do you want continue yes or no 'enter y or n'\n")

def ShowData(Data) :
    x = len(Data)
    if x == 0 :
        print("empty")
        nothing = input("\nenter any key to continue")
    else :
        for i in Data :
            print(i,end=",")
        nothing = input("\nenter any key to continue")

def RemoveData(Data,RData) :
    rm = input("enter the name who want to delete it\n")
    avaible = False
    for i in range(0,len(Data)) :
        if rm == Data[i] :
            avaible = True
            R = Data.pop(i)
            RData.append(R)
            print("remove succesfull")
        if avaible:
            nothing = input("\nenter any key to continue")
    if avaible == False :
        print("this name is not avaible")
        nothing = input("\nenter any key to continue")

def ShowRData(RData) :
    x = len(RData)
    if x == 0 :
        print("empty")
        nothing = input("\nenter any key to continue")
    else :
        for i in RData :
            print(i,end=",")
        nothing = input("\nenter any key to continue")


Data = []
RData = []
CH = int(input("1-Enter The Names\n\n2-Show Names\n\n3-Remove Name\n\n4-Show names whose removed\n\n5-Exit\n\n"))
os.system("cls")
while CH !=5 :
    if CH == 1 :
        EnterData(Data)
    elif CH == 2 :
        ShowData(Data)
    elif CH == 3 :
        RemoveData(Data,RData)
    elif CH == 4 :
        ShowRData(RData)
    else :
        print("this option not avaible")
    os.system("cls")
    CH = int(input("1-Enter The Names\n2-Show Names\n3-Remove Name\n4-Show names whose removed\n5-Exit\n"))
    os.system("cls")

print("program finished")