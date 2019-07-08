'''name = input ('what is your name? ')
color = input ('what is your favourite color? ')
print (f'{name} loves {color}')
print (name + ' loves ' + color)'''
'''weight = input ('what is your weight = ')
weight_lb = float (weight) * 0.45
print (weight_lb)'''
'''course = 'python for beginners oooh'
another = course [:]
print (another)'''
'''temp = input ('What is the temperature today: ')
if float (temp) > 25:
    print ('it is really hot out there
you should drink some water')
elif float(temp) < 25:
    print ('it is a cold day, wear thick clothes')
else:
    print ('it is a lovely day, enjoy it')'''
'''price = 1000000
customer_credit = input('do you have good credit: ')
deposit_10 = (10/100)*1000000
deposit_20 = (20/100)*1000000
if customer_credit == 'yes':
    print (f'make a deposit of {int(deposit_10)}naira')
else:
    print (f'make a deposit of {deposit_20}')'''
'''name = input ('Name: ')
if len(name) < 3:
    print('name must be at least three characters')
elif len(name) > 50:
    print('name can be maximum of 50 characters')
else:
    print('name is good')'''
'''weight = input ('Weight: ')
unit = input ('Lbs or Kg: ')
if unit.upper() == 'L':
    print (f'{int(weight)*0.45} kg is your weight')
elif unit.upper() == 'K':
    print (f'{int(weight)/0.45} Lbs is your weight')
else:
    print('please enter the correct value L or K')'''
'''instruction = ''
started = False
while True:
    instruction = input('> ')
    if instruction.lower() == 'start':
        if started:
            print ('car has already started....')
        else:
            started = True
            print ('car has  started')
    elif instruction.lower() == 'stop':
        if not started:
            print ('car has already stopped')
        else:
            started = False
            print ('car has stopped')
    elif instruction.lower() == 'help':
        print ('
start: to start the car
stop: to stop the car
quit: to end game')
    elif instruction.lower() == 'quit':
        break
    else:
        print ('sorry i dont understand')'''
'''prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print (f'total: {total} ')'''
numbers = [2,2,2,2,7]
for number in numbers:
    output = ''
    for count in range(number):
        output += 'x'
    print(output)

