'''
ADVENTURE GAME (4pts)
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import arcade

def computer_on():
    user_choice = input("Would you like to turn on the computer? (y/n) ")
    if user_choice.upper() == "Y" or user_choice.upper() == "YES":
        print("")
        answer = input("\033[1;34mYou turn on the computer. What is the password? ")
        print("")
        if answer == "DI3":
            print("Success! You find the employment logs. The last clown's name was... Oh no, some of the pixels are dead. You can only read ?A?IN.")
            answer = input("What is his name? \033[1;0m")
            if answer.upper() == "GAVIN":
                global known_identity
                known_identity = True
                print("")
                print("\033[1;32mCorrect!\033[1;34m Now only if you had a key to unlock the entrance...")
                print("You feel a strong urge to use the bathroom now. Not even the smell could get in the way.\033[1;0m")
            else:
                print("\033[1;31mWRONG!\033[1;0m")
        else:
            print("")
            print("\033[1;31mWRONG!\033[1;0m")
    elif user_choice.upper() == "N" or user_choice.upper() == "NO":
        print("\033[1;34mMaybe there's a better time.\033[1;0m")
    else:
        print("\033[1;34mI don't understand what you typed.\033[1;0m")

def inventory_check():
    inventory_list = ""
    for item in inventory:
        negative_index = (len(inventory) - inventory.index(item)) * -1
        if len(inventory) == 1 or negative_index == -1:
            inventory_list += f"{item}"
        else:
            inventory_list += f"{item}, "
    if inventory_list == "":
        print("You have nothing in your inventory!")
    else:
        print(f'''Inventory: {inventory_list}''')

#game setup
room_list = []
current_room = 0
inventory = []
help_center_unlock = False #checks if the help center is locked or unlocked
known_identity = False #checks if the user has figured out the clown's name
done = False

#Entrance
room = ["Entrance: Something about the rusty gate gives you the creeps. It looks deceivingly weak, but it definitely wouldn't budge if it was locked...", 2, None, None, None, "\033[1;34mIt's locked!\033[1;0m"]
room_list.append(room)

#Potty
room = ["Potty: The reak of urine fills the air. You kind of feel the need to go, but you don't want to see what's in there.", 4, 2, None, None, "\033[1;34mIt's nasty!\033[1;0m"]
room_list.append(room)

#Ticket Booth
room = ["Ticket Booth: A lone pink ticket booth stands at the center of the plaza.", 5, 3, 0, 1, "\033[1;34mThere's a hole in the window just large enough that you could probably stick your hand in there. However, the sharp glass would probably cut you up.\033[1;0m"]
room_list.append(room)

#Help Center
room = ["Help Center: What used to be the help center of the carnival is nothing but a rundown abandoned building.", 6, None, None, 2, "\033[1;34mYou go around the back, but the door is locked.\033[1;0m"]
room_list.append(room)

#Stage
room = ["Stage: Amazed at the sheer size of the stage, you couldn't help but wonder what kind of artists performed on there.", 7, 5, 1, None, "\033[1;34mYou see a loose curtain covering the back of the stage. There seems to be a red liquid oozing from the bottom.\033[1;0m"]
room_list.append(room)

#Concessions
room = ["Concessions: Food! You see all of the booths that used to sell fair food. Your stomach begins to rumble thinking about funnel cakes, fried oreos, and corndogs.", 8, 6, 2, 4, "\033[1;34mThe door to the corndog stand is ajar.\033[1;0m"]
room_list.append(room)

#Fortune
room = ["Fortune: You jump at the sight of a man inside the fortune teller box just to realize it's a stupid robot.", 9, None, 3, 5, "\033[1;34mThe robot looks like it still works.\033[1;0m"]
room_list.append(room)

#Roller Coaster
room = ["Roller Coaster: Woah... It's the tallest roller coaster you've ever seen!", None, 8, None, None, "\033[1;34mYou search around the premise and see a hole in the fence.\033[1;0m"]
room_list.append(room)

#Carousel
room = ["Carousel: The colorful horses remind you of your childhood. You wonder if the ride still works.", 10, 9, 5, 7, "\033[1;34mYou find a button and click it. The ride does work!\033[1;0m"]
room_list.append(room)

#Circus
room = ["Circus: The bright colors of the tent blind you.", None, None, 6, 8, "\033[1;34mYou enter the tent and see a large curtain draping over a structure.\033[1;0m"]
room_list.append(room)

#Ferris Wheel
room = ["Ferris Wheel: The main attraction. The ferris wheel overlooks all of the park. The ride still looks like it's in good condition.", None, None, 8, None, "\033[1;34mYou search around and find the lever that activates the whole ride.\033[1;0m"]
room_list.append(room)

print("\033[1;36mAn ominous mist engulfs the amusement park in front of you. Over the course of three months, multiple children have gone missing in your town.")
print("As an aspiring investigator, you noticed that they all had one connection. The last photos ever seen of the kids are with a clown at the amusement park.")
print("Discover the clown's identity.\033[1;0m")

while not done:
    print("")
    print(room_list[current_room][0])
    user_choice = input('''What would you like to do?:
N. North
E. East
S. South
W. West
I. Inspect
C. Check Inventory
Q. Quit
Choice: ''')

#user_choice directions
#Going North
    if user_choice.upper() == "N" or user_choice.upper() == "NORTH":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("")
            print("You can't go that way!")
        else:
            current_room = next_room

#Going East
    elif user_choice.upper() == "E" or user_choice.upper() == "EAST":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("")
            print("You can't go that way!")
        else:
            current_room = next_room

#Going South
    elif user_choice.upper() == "S" or user_choice.upper() == "SOUTH":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("")
            print("You can't go that way!")
        else:
            current_room = next_room

#Going West
    elif user_choice.upper() == "W" or user_choice.upper() == "WEST":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("")
            print("You can't go that way!")
        else:
            current_room = next_room

#Inspecting
    elif user_choice.upper() == "I" or user_choice.upper() == "INSPECT":
        print("")
        if current_room == 3 and help_center_unlock == True:
            print("\033[1;34mYou enter the help center.\033[1;0m")
            computer_on()
        else:
            print(room_list[current_room][5])  # print inspect description for whatever room player is in

#action for entrance room
        if current_room == 0:
            if "entrance key" in inventory:
                print("\033[1;34mHowever, you have the key! You unlock the gate and drive straight to the police station.\033[1;0m")
                print("\033[1;32mYou won!")
                done = True
            else:
                continue

#action for potty
        if current_room == 1:
            print("")
            if known_identity == True:
                print("\033[1;34mYou have to go so bad that you enter the porta potty. As you look down the hole, you see a shiny object.\033[1;0m")
                print("")
                user_choice = input("Would you like to grab the shiny object? (y/n)  ")
                if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                    print("\033[1;34mYou reach into the hole... Gross... and grab the \033[1;33mentrance key\033[1;34m!\033[1;0m")
                    inventory.append("entrance key")
            else:
                print("\033[1;34mThe whiff of urine is too nauseating to enter the potty. You should explore other areas.\033[1;0m")


#action for ticket booth
        if current_room == 2: #action for ticket booth
            print("")
            user_choice = input("Would you like to stick your hand in the window? (y/n) ")
            if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                print("\033[1;34mYou stick your hand carefully into the window. You search around the desk, and you discover the \033[1;33mhelp center key\033[1;34m!\033[1;0m")
                inventory.append("help center key") #add the key to the help center to the inventory list
            elif user_choice.upper() == "N" or user_choice.upper() == "NO":
                print("\033[1;34mIt's not a good idea. You continue on your search.\033[1;0m")
            else:
                print("\033[1;34mI don't understand what you typed.\033[1;0m")

#action for help center
        if current_room == 3 and "help center key" in inventory:
            help_center_unlock = True
            print("")
            print("\033[1;34mWith the key you obtained from the ticket booth, you open up the help center and walk inside.\033[1;0m")
            inventory.remove("help center key")
            print("")
            computer_on()

#action for stage
        if current_room == 4:
            print("")
            user_choice = input("You walk on top of the brightly lit stage. Would you like to pull down the curtain? (y/n) ")
            if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                print("\033[1;34mYou pull down the curtain and uncover a big and bloody \033[1;31mV\033[1;34m. What can this mean? Vendetta?\033[1;0m")
            elif user_choice.upper() == "N" or user_choice.upper() == "NO":
                print("\033[1;34mSomething is telling you to not pull down the curtain...\033[1;0m")
            else:
                print("\033[1;34mI don't understand what you typed.\033[1;0m")

#action for concessions
        if current_room == 5:
            print("")
            user_choice = input("Would you like to enter the corndog stand? (y/n) ")
            if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                print("\033[1;34mYou walk into the corndog stand and see a perfectly preserved \033[1;33mcorndog\033[1;34m on the table! You grabbed it because you are so hungry.\033[1;0m")
                inventory.append("corndog")
            elif user_choice.upper() == "N" or user_choice.upper() == "NO":
                print("\033[1;34mThere's definitely something creeping in there... Better avoid it...\033[1;0m")
            else:
                print("\033[1;34mI don't understand what you typed.\033[1;0m")

#action for fortune
        if current_room == 6:
            print("")
            if "quarter" not in inventory:
                print("\033[1;34mYou take a closer look and see there's a slot for a quarter. Maybe there's one lying around.\033[1;0m")
            elif "quarter" in inventory:
                user_choice = input("Would you like to insert your quarter into the fortune teller's box? (y/n) ")
                if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                    print("")
                    inventory.remove("quarter")
                    print("\033[1;34mYou insert the quarter, and the robot rises eerily.")
                    print('''Fortune Teller: Hello human.
                    
The robot let out a sinister chuckle.

Fortune Teller: It's not safe here... There's a reason this carnival is shut down for good. I've been trapped here for ten years. At least I won't be the only one.

The robot chuckles again.

Fortune Teller: The clown is close... He's in the pot@F4jW4Lk2!

The robot's voice becomes twisted, jumping between octaves. Sparks begin flying out of its head.

Fortune Teller: *5rj;WPoS...you're dead.

The robot explodes into flames. However, a small sheet of paper prints from the bottom of the box. On it is a bloody \033[1;31mG\033[1;0m.
''')
                elif user_choice.upper() == "N" or user_choice.upper() == "NO":
                    print("\033[1;34mMaybe you can save the quarter for something else.\033[1;0m")
                else:
                    print("\033[1;34mI don't understand what you typed.\033[1;0m")
            else:
                print("\033[1;34mI don't understand what you typed.\033[1;0m")

#action for roller coaster
        if current_room == 7:
            print("")
            user_choice = input("Would you like to enter the hole in the fence? (y/n) ")
            if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                print("\033[1;34mYou enter the hole in the fence and search underneath the rollercoaster rails. You see a bunch of loose change everyone dropped from above. Penny... Nickel... Dime... Bingo! You find a \033[1;33mquarter\033[1;34m!\033[1;0m")
                inventory.append("quarter")
            elif user_choice.upper() == "N" or user_choice.upper() == "NO":
                print("\033[1;34mYou decide against entering the hole in the fence. What if the clown is in there? What if the roller coaster activates and takes off your head while you're underneath it?\033[1;0m")
            else:
                print("\033[1;34mI don't understand what you typed.\033[1;0m")

#action for carousel
        if current_room == 8:
            print("")
            user_choice = input("Would you like to ride the carousel? (y/n) ")
            if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                user_choice = input('''Which horse will you pick?
A. Red
B. Yellow
C. Blue
Choice: ''')
                if user_choice.upper() == "A" or user_choice.upper() == "RED":
                    print("\033[1;34mYou hop onto the red horse and see there's a letter engraved into the horse's neck: \033[1;35mD\033[1;34m. Weird.\033[1;0m")
                elif user_choice.upper() == "B" or user_choice.upper() == "Yellow" or user_choice.upper() == "C" or user_choice.upper() == "BLUE":
                    print("\033[1;34mYou hop onto your horse and have a fun time riding the ride. However, it breaks down after only a few minutes.\033[1;0m")
                else:
                    print("\033[1;34mI don't understand what you typed.\033[1;0m")
            elif user_choice.upper() == "N" or user_choice.upper() == "NO":
                 print("\033[1;34mMaybe it's a good idea not to ride the carousel. It might break.\033[1;0m")
            else:
                print("\033[1;34mI don't understand what you typed.\033[1;0m")

#action for circus
        if current_room == 9:
            print("")
            user_choice = input("Would you like to pull down the curtain? (y/n) ")
            if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                print("\033[1;34mYou pull down the curtain and see a lion sleeping in a cage. Next to the lion is a piece of paper. Is it a code?\033[1;0m")
                circus_continue = True
                while circus_continue:
                    print("")
                    user_choice = input("Do you have anything in your inventory to distract the lion? (q for quit or c for check inventory) ")
                    if user_choice.upper() == "CORNDOG" or user_choice.upper() == "CORN DOG" and "corndog" in inventory:
                        inventory.remove("corndog")
                        print("\033[1;34mYou throw the corndog across the cage. First the sound catches the lion's attention and then the smell.\033[1;0m")
                        print("")
                        user_choice = input("Would you like to enter the cage? (y/n) ")
                        if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                            print("\033[1;34mYou creep into the cage carefully. You grab the piece of paper and sprint out before the lion could finish the corndog.\033[1;0m")
                            print("\033[1;34mYou look at the piece of paper. The only letter on it is an \033[1;35mI\033[1;34m. It's worthless!\033[1;0m")
                            circus_continue = False
                        elif user_choice.upper() == "Y" or user_choice.upper() == "YES":
                            print("\033[1;34mMaybe it's a good idea not to be in the same vicinity as a lion.\033[1;0m")
                        else:
                            print("\033[1;34mI don't understand what you typed.\033[1;0m")
                    elif user_choice in inventory and user_choice != "corndog":
                            print("\033[1;34mI don't think you can use that.\033[1;0m")
                    elif user_choice.upper() == "Q" or user_choice.upper() == "QUIT":
                        print("\033[1;34mYou walk out of the tent. Maybe you can find something out here.\033[1;0m")
                        circus_continue = False
                    elif user_choice.upper() == "C" or user_choice.upper() == "CHECK" or user_choice.upper() == "CHECK INVENTORY":
                        inventory_check()
                    else:
                        print("\033[1;34mI don't understand what you typed.\033[1;0m")

#action for ferris wheel
        if current_room == 10:
            print("")
            user_choice = input("Would you like to take a ride? (y/n) ")
            if user_choice.upper() == "Y" or user_choice.upper() == "YES":
                print("\033[1;34mYou take a relaxing ride to the top. You can see the whole park from here! As you look closer, you realize the stage lights spell something. It spells out a \033[1;35m3\033[1;0m.")
                print("\033[1;34mAs the ride descends you wonder what it could mean. You exit the ride.\033[1;0m")
            elif user_choice.upper() == "N" or user_choice.upper() == "NO":
                print("\033[1;34mMaybe it's better not. What if the whole ferris wheel collapsed?\033[1;0m")
            else:
                print("\033[1;34mI don't understand what you typed.\033[1;0m")

#Checking Inventory
    elif user_choice.upper() == "C" or user_choice.upper() == "CHECK" or user_choice.upper() == "CHECK INVENTORY":
        print("")
        inventory_check()

#User chooses to quit
    elif user_choice.upper() == "Q" or user_choice.upper() == "QUIT":
       done = True
    else:
        print("")
        print("\033[1;34mSorry. I don't know what direction that is. Try again.\033[1;0m")



