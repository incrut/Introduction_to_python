phone_book = {'Emergency number': '112'}

while True:
    answer = input ('Enter a name (done to quit) ')
    
    if answer.lower() == 'done':
        print ('The phone book has %i entries in it' %( len(phone_book)))
        print ('All records in the phone book:', phone_book)
        for name, number in phone_book.items():
            print (name + ':', number)
        break
    
    else:
        if answer in phone_book:
            print ('There is already {0} in your phone book with number {1}'.format(answer, phone_book[answer]))
            ans = input ('Do you want to update it or delete it? (upd/del/no)')
            
            if ans.lower() == 'upd':
                phone_book[answer] = input ('Enter a new number ')
                
            elif ans.lower() == 'del':
                del phone_book[answer]
                
            elif ans.lower() == 'no':
                pass
            
            else:
                print ('There is no such option please check the spelling of your answer')
        
        
        else:
            print ('There is no such contact in your phone book')
            ans = input ('Do you want to create a new one? (yes/no) ')
            if ans.lower() == 'yes':
                phone_book [answer] = input ('Enter a number ')
                
            elif ans.lower() == 'no':
                pass
            
            else:
                print ('There is no such option please check the spelling of your answer')
            
            