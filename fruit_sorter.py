i=1
apples=0
oranges=0
olives=0
while i<=10:
    i=i+1
    print('---------------')
    new_fruit=input('Enter Name Of Fruit: ')
    print('---------------')
    print('  ')
    if (new_fruit=='Apples'):
        print('Apples Must Move to Bin1')
        apples=apples+1
    elif (new_fruit=='Orange'):
        print('Oranges Must Move to Bin2')
        oranges=oranges+1
    elif (new_fruit=='Olives'):
        print('Olives Must Move to Bin3')
        olives=olives+1
    else :print('Confused Not Spicefied.')
    
print('You have inserted exactly 10 Fruits.')
print('Apples:', apples)
print('Oranges:', oranges)
print('Olives:', olives)
