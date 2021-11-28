name = input("Enter your name: ")
print("Greetings", name, "welcome to the land of Landyn Easome")  

answer = input( "Would you like to start your journey? (yes/no) ")

if answer.lower().strip() == "yes":


    answer = input("The towns elder is looking for you, would you like to look for him yes or no?")
    if answer == "yes":
        answer = input("The elder has giving you a quest, would you like to accept the quest or deny it")

        if answer == "accept":
            print("Thank you", name, "ever since we lost the war of Westscott, We've been relying on our selves.")
        else:
            print("I knew I couldn't count on you")

answer = input("Would you like to hear the story of Westscott? (yes/no) ")

if answer.lower().strip() == "yes":
    print("There was an ancient battle that happend in our land, roughly 3,500 years ago. There was a man who wanted to take over the king, the man was known as one of the Necromancers. There was only a handful in our kingdom.")
else:
    print("We'll save that for a different day")

answer = input("There was a loud explosion outside the wall, it sounds like there is a crowd approaching, would you like to go outside the walls? (yes/no)")
if answer.lower().strip() == "yes":
        print("The elder is dead")

