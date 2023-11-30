import random

score = 0

while True:
    num = random.randint(1,10)
    answer = input ('guess the number ')
    
    try:
        answer = int(answer)
    except:
        answer = answer.lower()
        
    if answer == num:
        score += 1
        print ('Yes you are right')

    elif answer == 'quit':
        break

    else:
        print ('No you\'re wrong')
    
    print ('Your score is', score)