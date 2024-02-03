#Madlibs !!
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
        verb1_3= input("type a verb: ")
        body1_1 = input("type a part of the body (plural): ")
        noun1_2 = input("type a noun (plural): ")
        verb1_4 = input("type a verb: ")
        noun1_3 = input("type a noun: ")
        
        print(" ")
        print(f"It was a {adj1_1}, cold November day. I woke up to the {adj1_2} smell")
        print(f"of {bird1_1} roasting downstairs. I {verb1_1} down the stairs to see if I could")
        print(f'help {verb1_2} the dinner. My mom said, "See if {name1_1} needs a fresh {noun1_1}."')
        print(f"So I carried a tray of glasses full of {liquid1_1} into the {verb1_3}ing room.")
        print(f"When I got there, I couldn't believe my {body1_1}! There were {noun1_2} {verb1_4}ing on the {noun1_3}.")
        print(" ")
        
        while True:
            again1 = input('Would you like to do this Madlib again? (y/n): ')
            if again1 == 'n':
                start()       
            elif again1 == 'y':
                break
            else:
                print("Wrong input.")

def mad2():
    while True:
        # Input
        liquid2_1 = input("type a liquid: ")
        adj2_1 = input("type an adjective: ")
        num2_1 = input("type a number: ")
        adj2_2 = input("type an adjective: ")
        noun2_1 = input("type a noun: ")
        adj2_3 = input("type an adjective: ")
        adj2_4 = input("type another adjective: ")
        food2_1 = input("type a food: ")
        adj2_5 = input("type an adjective: ")
        adj2_6 = input("type another adjective: ")
        body2_1 = input("type a part of the body: ")
        noun2_2 = input("type a noun: ")
        adj2_7 = input("type an adjective: ")
        verb2_1 = input("type a verb: ")
        noun2_3 = input("type a noun (plural): ")
        place2_1 = input("type a place: ")
        verb2_2 = input("type a verb: ")
        
        # Output
        print(' ')
        print(f"When you show up for a rooftop party, the {liquid2_1} you choose to")
        print(f"drink is very important. After all, the weather is usually {adj2_1}, the")
        print(f"party lasts for {num2_1} hours, and don't want to get {adj2_2} too early.")
        print(f"So what should you drink? You take a look in the cooler, and the first {noun2_1}")
        print(f"you come across is a stout. You usually love to drink such a dark, {adj2_3} beer,")
        print(f"but it might be a little too {adj2_4} for this occasion. You don't want to")
        print(f"feel like you just ate a loaf of {food2_1}. What about a wheat beer? It seems")
        print(f"like the most {adj2_5} choice for a summer party. You love the {adj2_6} taste,")
        print(f"but it also gives you a raging {body2_1}-ache. In the end you choose a {noun2_2.capitalize()} Light,")
        print(f"your usual go-to. It's {adj2_7}, easy to {verb2_1}, and goes down with all")
        print(f"the {noun2_3} you plan to eat. Only problem is you might have to make more trips")
        print(f"to (the) {place2_1} than usual - {noun2_2.capitalize()} Light makes you {verb2_2} all night long!")
        print(' ')
        
        # Play again?
        while True:
            again2 = input('Would you like to do this Madlib again? (y/n): ')
            if again2 == 'n':
                start()       
            elif again2 == 'y':
                break
            else:
                print("Wrong input.")
        
def mad3():
    while True:
        name3_1 = input("enter a man's name: ")
        occ3_1 = input("enter an occupation: ")
        noun3_1 = input("enter a noun: ")
        noun3_2 = input("enter another noun: ")
        noun3_3 = input("enter another noun: ")
        shape3_1 = input("enter a shape: ")
        verb3_1 = input("enter a verb: ")
        name3_2 = input("enter a woman's name: ")
        body3_1 = input("enter a body part: ")
        verb3_2 = input("enter a verb: ")
        noun3_4 = input("enter a noun: ")
        noun3_5 = input("enter another noun: ")
        place3_1 = input("enter a restaurant name: ")
        hist3_1 = input("enter a historic monument: ")
        verb3_3 = input("enter a verb: ")
        noun3_6 = input("enter a noun: ")
        noun3_7 = input("enter another noun: ")
        noun3_8 = input("enter another noun: ")
        verb3_4 = input("enter a verb: ")
        noun3_9 = input("enter a noun: ")
        adj3_1 = input("enter an adjective: ")
        adj3_2 = input("enter another adjective: ")
        emo3_1 = input("enter an emotion: ")
        verb3_5 = input("enter a verb: ")
        noun3_10 = input("enter a noun: ")
        noun3_11 = input("enter another noun: ")
        verb3_6 = input("enter a verb: ")
        
        print(' ')
        print(f"{name3_1.capitalize()} is a normal {occ3_1}. Then one day, a {noun3_1} explodes,")
        print(f"causing a {noun3_2} to blow up, and a nearby {noun3_3} erupts into a")
        print(f"{shape3_1} of flames. {name3_1.capitalize()} realizes that he's being chased by the government,")
        print(f"who's trying to {verb3_1} him. While on the run, he teams up with an")
        print(f"incredibly attractive woman named {name3_2.capitalize()}, who has an incredible {body3_1}.")
        print(f"She may be from the streets, but she can {verb3_2} like nobody's buisness. The duo")
        print(f"decide to turn thd tables on their pursuers by blowing up a {noun3_4}, which triggers")
        print(f"a chain reaction, causing the local {noun3_5}, {place3_1}, and the {hist3_1} to  explode.")
        print(f"Then, the bad guys' helicopter gets {verb3_3} by a piece of {noun3_6} from when the {noun3_7}")
        print(f"exploded, and the helicopter explodes and falls onto a {noun3_8}, causing it to {verb3_4},")
        print(f"which shoots a fireball straight into the heart of {noun3_9} and destroys the bad guy leader.")
        print(f"Everything is {adj3_1} and the two decide that such a {adj3_2} ordeal has caused them to fall")
        print(f"in {emo3_1} with each other. They decide to celebrate by {verb3_5}ing on the {noun3_10} and they")
        print(f"even managed to use a {noun3_11} from the beginning of the movie, to {verb3_6} the whole story back together.")
        print(' ')
        
        while True:
            again3 = input('Would you like to do this Madlib again? (y/n): ')
            if again3 == 'n':
                start()       
            elif again3 == 'y':
                break
            else:
                print("Wrong input.")
        
def mad4():
    while True:
        animal4 = input("enter an animal: ")
        food4_1 = input("enter a food: ")
        noun4_1 = input("enter a noun: ")
        verb4_1  = input("enter a verb: ")
        verb4_2 = input("enter another verb: ")
        verb4_3 = input("enter another verb: ")
        verb4_4 = input("enter yet another verb: ")
        noun4_2 = input("enter a noun: ")
        place4_1 = input("enter a location: ")
        noun4_3 = input("enter a noun: ")
        noun4_4 = input("enter a noun: ")
        place4_2 = input("enter a location: ")
        verb4_5 = input("enter a verb: ")
        food4_2 = input("enter a food: ")
        game4 = input("enter a game: ")
        verb4_6 = input("enter a verb: ")
        noun4_5 = input("enther a noun: ")
        noun4_6 = input("enter another noun: ")
        noun4_7 = input("enter another noun (plural): ")
        verb4_7 = input("enter a verb ending in -ing: ")
        verb4_8 = input("enter a verb: ")
        noun4_8 = input("enter a noun (plural): ")
        verb4_9 = input("enter a verb: ")
        
        print(' ')
        print(f"If you give a {animal4} a {food4_1}, they are going to ask for a {noun4_1}.")
        print(f"When you give them the {noun4_1}, they will want to {verb4_1}. When they are finished,")
        print(f"they will {verb4_2}. Then they will {verb4_3} and {verb4_4} to the {noun4_2}. Since that")
        print(f"doesn't work out, they will want to go to {place4_1}. On the way, they will see a {noun4_3}")
        print(f"and will want {noun4_4}. Then you will have to take them to the {place4_2}. They will {verb4_5}.")
        print(f"When they are done, they will ask you for some {food4_2}. On the way home they will start a game of")
        print(f"{game4}. When you finally get home, you'll have to {verb4_6}. Then they will want a {noun4_5}.")
        print(f"You'll have to find a {noun4_6} and {noun4_7}. When they see the {noun4_7}, they will start {verb4_7}.")
        print(f"Then they will {verb4_8} out of {noun4_8}. Of course, when they are finished they will want to {verb4_9}.")
        print(f"So they will ask for a {noun4_1}. And chances are if you give them a {noun4_1}, they are going to want a {food4_1}.")
        print(' ')
        
        while True:
            again4 = input('Would you like to do this Madlib again? (y/n): ')
            if again4 == 'n':
                start()       
            elif again4 == 'y':
                break
            else:
                print("Wrong input.")
        

# Madlib Bank




#Start Screen
def start():
    while True:
        print('Choose a madlib.')
        print(' ')
        print('1. Help Mom with Cooking')
        print('2. The Best Beer Choice')
        print('3. Michael Bay Movie')
        print('4. If You Give A..')
        print(' ')
        print("type 'end' to leave.")

        while True:
            choose = input("(1-4): ")
            if choose == 'end':
                break
            elif not choose.isdigit():
                print("     Wrong Input. Please enter a number.")
            elif choose.isdigit():
                break
        
        if choose == 'end':
            run = False
            break
            
        if int(choose) > 4 or int(choose) < 1:
            print("     Please enter a number between 1 and 4.")
            while True:
                choose = input("(1-4): ")
                if choose == 'end':
                    break
                if not choose.isdigit():
                    print("     Wrong Input. Please enter a number.")
                elif int(choose) > 4 or int(choose) < 1:
                    print("     Please enter a number between 1 and 4.")
                elif int(choose) >= 1 and int(choose) <= 4:
                    break

        if choose == '1':
            mad1()
        if choose == '2':
            mad2()
        if choose == '3':
            mad3()
        if choose == '4':
            mad4()
        if choose == 'end':
            break

start()
