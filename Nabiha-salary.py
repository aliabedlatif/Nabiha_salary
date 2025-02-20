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
print(f"The amount save is {save}$ ,the amount rent is {rent}$, the amount electricty is {electricty}$ ")
sum = save + rent + electricty
print(f"The total amount of nabiha is {sum}$")
remainder_salary = salary - sum
print(f"the remainder of nabiha salary after these expenses is {remainder_salary}$")
yearly = (rent + electricty)*(12)