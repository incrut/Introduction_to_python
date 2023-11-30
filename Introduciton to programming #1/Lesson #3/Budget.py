def budget(PP) :
    Money=PP*10+55
    return Money
inv=int(input("Please enter the number of invited people "))
att=int(input("Please enter the number of people attending "))
print("Maximum budget is ",budget(inv),"EUROS")
print("Minimum budget is ",budget(att),"EUROS")