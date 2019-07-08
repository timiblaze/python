#this is an exercise from the video, i solved
name = input ('what is your name? ')
color = input ('what is your favourite color? ')
print (f'{name} loves {color}')
print (name + ' loves ' + color)
#exercise 2
weight = input ('what is your weight = ')
weight_lb = float (weight) * 0.45
print (weight_lb)
#exercise 3
course = 'python for beginners oooh'
another = course [:]
print (another)
#exercise 4
weight = input ('Weight: ')
unit = input ('Lbs or Kg: ')
if unit.upper() == 'L':
    print (f'{int(weight)*0.45} kg is your weight')
elif unit.upper() == 'K':
    print (f'{int(weight)/0.45} Lbs is your weight')
else:
    print('please enter the correct value L or K')
    
