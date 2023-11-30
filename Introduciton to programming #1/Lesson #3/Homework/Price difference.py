def price_difference (a, b, c):
    price = a
    monthly = b
    numths = c
    difference = (monthly * numths) - price
    return difference
P = int (input ('Write the initial price '))
M = int (input ('What is the monthly payment of the first installment plan? '))
N = int (input ('How many months does the first installment plan last? '))
diff1 = price_difference (P, M, N)
print ('The overpayment for the first installment plan is', diff1)
M = int (input ('What is the monthly payment of the second installment plan? '))
N = int (input ('How many months does the second installment plan last? '))
diff2 = price_difference(P, M, N)
print ('The overpayment for the first installment plan is', diff2)
if diff1 < diff2:
    print ('The first installment plan is better')
elif diff1 > diff2:
    print ('The second installment plan is better')