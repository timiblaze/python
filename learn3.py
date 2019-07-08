#exercise 5   
price = 1000000
customer_credit = input('do you have good credit: ')
deposit_10 = (10/100)*1000000
deposit_20 = (20/100)*1000000
if customer_credit == 'yes':
    print (f'make a deposit of {int(deposit_10)}naira')
else:
    print (f'make a deposit of {deposit_20}')
#exercise 6
name = input ('Name: ')
if len(name) < 3:
    print('name must be at least three characters')
elif len(name) > 50:
    print('name can be maximum of 50 characters')
else:
    print('name is good')
#exercise 6 which prints out x's in the shape of an l.
numbers = [2,2,2,2,7]
for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)