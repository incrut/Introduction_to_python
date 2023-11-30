suits = ('♥', '♦', '♣', '♠')
ranks = ('A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2')

cards = []

for suits in suits:
    for rank in ranks:
        cards.append((suit, rank))
        
        
for s, r in cards:
    print (r, s)
        
#print (cards)