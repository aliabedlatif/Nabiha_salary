salary = int(input("Enter salary of month:"))
Month = input("Enter name of month:")
percentage = input("Enter price for a)saving , b)rent ,c)electricty:")
while percentage != "d":
    if percentage == "a":
        save = int(input("the amount saving:"))
    elif percentage == "b":
        rent = int(input("the amount rent:"))
    elif percentage == "c":
        electricty = int(input("the amount electricty:"))
    percentage = input("enter price a)saving b)rent c)electricty: ")