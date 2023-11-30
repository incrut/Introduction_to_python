# functions

def total_price(stocks):
    total = 0
    for stock in stocks:
        total += stock[1] * stock[2]
    return total

def profit(stonks):
    total_profit = 0
    for stock in stonks:
        total_profit += stock[2] * stock[4] - stock[2] * stock[1]

    return total_profit




portfolio = [
( "25-Nov-2019", 43.50, 25, "CAT", 92.45 ),
( "25-Nov-2019", 42.80, 50, "DD", 51.19 ),
( "25-Nov-2019", 42.10, 75, "EK", 34.87 ),
( "25-Nov-2019", 37.58, 100, "GM", 37.58 ),
]

portfolio_2 = [
( "25-Nov-2019", 43.50, 25, "CAT", 12.45 ),
( "25-Nov-2019", 42.80, 50, "DD", 41.19 ),
( "25-Nov-2019", 42.10, 75, "EK", 34.87 ),
( "25-Nov-2019", 37.58, 100, "GM", 37.58 ),
]


print(total_price(portfolio))
port_1 = profit(portfolio)
port_2 = profit(portfolio_2)

if port_1 > 0:
    print("Profit is", port_1)

elif port_1 < 0:
    print("Loss is", profit_2)

else:
    print("No gain or loss.")