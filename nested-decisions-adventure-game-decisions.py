#question 1 task 1

place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: 
        print("You found a boat!")
else:
    print("You found a hidden treasure!")


#question 1 task 2

place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: 
        print("You found a boat!")
else:
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found a hidden treasure!")
    else:
        print("Sorry, you fell in a hole")


# question 1 task 3

place = input("Choose a place: forest or cave?")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river": 
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("Sorry, you fell in a hole")
    else: 
        pass
else:
    pass