diameter = input ("What is the diameter of your pizza? ")
total_price = input ("How many euros does it cost? " )

try :
    diameter2 = int(diameter)
    total_price2 = float(total_price)
    answer = round(total_price2/(3.14*(diameter2/2)**2)*100, 2)
    print("One square centimetre of your pizza costs", answer, "eurocents")


except:
    print("Not a number")

        