def receive_cm(cm):
    print(cm)
    if cm.isdigit():
        print('Validate')
    else:
        print('This text is not a digit')
    

def receive_tank(tank_variable):
    print(tank_variable)
    if tank_variable == 0:
        print('15-15-30')
    elif tank_variable == 1:
        print('10-10-10-30')
    else:
        print("ERROR")