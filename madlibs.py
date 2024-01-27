#Madlibs !!
run = True
print(' ')
print(' ')
print('Welcome to Madlibs!')
print(' ')
print(' ')

# Madlib Bank

def mad1():
    while True:
        adj1_1 = input("type an adjective: ")
        adj1_2 = input("type another adjective: ")
        bird1_1 = input("type a type of bird: ")
        verb1_1 = input("type a verb in the past tense: ")
        verb1_2 = input("type a verb: ")
        name1_1 = input("type a relative's name: ")
        noun1_1 = input("type a noun: ")
        liquid1_1 = input("type a liquid: ")
        verb1_3= input("type a verb ending in -ing: ")
        body1_1 = input("type a part of the body (plural): ")
        noun1_2 = input("type a noun (plural): ")
        verb1_4 = input("type a verb ending in -ing: ")
        noun1_3 = input("type a noun: ")

        print(f"It was a {adj1_1}, cold November day. I woke up to the {adj1_2} smell")
        print(f"of {bird1_1} roasting downstairs. I {verb1_1} down the stairs to see if I could")
        print(f'help {verb1_2} the dinner. My mom said, "See if {name1_1} needs a fresh {noun1_1}."')
        print(f"So I carried a tray of glasses full of {liquid1_1} into the {verb1_3} room.")
        print(f"When I got there, I couldn't believe my {body1_1}! There were {noun1_2} {verb1_4} on the {noun1_3}.")
        
        again1 = input('Would you like to do this Madlib again? (y/n): ')
        if again1 != 'y' or 'n':
            while True:
                print(' Wrong Input...')
                again1 = input('Would you like to do this Madlib again? (y/n): ')
                if again1 == 'y' or 'n':
                    break
                else:
                    continue
                
        elif again1 == 'y':
            continue
        elif again1 == 'n':
            break

        

def mad2():
    print('You selected 2')

def mad3():
    while True:
        print('You selected 3')

def mad4():
    while True:
        print('You selected 4')

def mad5():
    while True:
        print('You selected 5')

# Madlib Bank




#Start Screen

while run == True:
    print('Choose a madlib.')
    print(' ')
    print('1. ')
    print('2. ')
    print('3. ')
    print('4. ')
    print('5. ')
    print(' ')
    print("type 'end' to leave.")
    
    while True:
        choose = input("(1-5): ")
        if not choose.isdigit():
            print("     Wrong Input. Please enter a number.")
        elif choose.isdigit() or 'end':
            break
    
    if choose == 'end':
        run = False
        break
        
    if int(choose) > 5 or int(choose) < 1:
        print("     Please enter a number between 1 and 5.")
        while True:
            choose = input("(1-5): ")
            if not choose.isdigit():
                print("     Wrong Input. Please enter a number.")
            elif int(choose) > 5 or int(choose) < 1:
                print("     Please enter a number between 1 and 5.")
            elif int(choose) >= 1 and int(choose) <= 5:
                break
            
    
    if choose == '1':
        mad1()
    if choose == '2':
        mad2()
    if choose == '3':
        mad3()
    if choose == '4':
        mad4()
    if choose == '5':
        mad5()
