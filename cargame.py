instruction = ''
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
        print ('''
start: to start the car
stop: to stop the car
quit: to end game''')
    elif instruction.lower() == 'quit':
        break
    else:
        print ('sorry i dont understand')