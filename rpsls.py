# Rock-paper-scissors-lizard-Spock

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print "Name invalid!!!"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print "Number invalid!!!"
    

def rpsls(player_choice):   
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_name = number_to_name(comp_number)
    print "Player choose", player_choice
    print "Computer chooses", comp_name
    difference = (player_number - comp_number) % 5
    if difference == 1 or difference == 2:
        print "Player wins!\n"
    elif difference == 0:
        print "Player and computer tie!\n"
    else:
        print "Computer wins!\n"
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")





