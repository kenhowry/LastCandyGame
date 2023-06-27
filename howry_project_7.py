"""
Last Candy Game:
Two players take turns picking candy out of boxes until there is none left. 
The player who takes the last piece of candy is the winner.

File Name: howry_project_7.py
Author: Ken Howry
Date: 22.10.28
Course: COMP 1351
Assignment: Project VII
Collaborators: N/A
Internet Source: N/A
"""

#variables
candies = []
turn = 1
candy_selection = False
box_selection = False

#making the list
for i in range(6):
    candies.append(7)

#beginning of game
print("There are 6 boxes, each containing 7 pieces of candy.\nTwo players take turns.\nOn your turn, choose a box, and enter how many candies you want to take from that box.\nYou must take at least one piece of candy.\nThe person who takes the last piece wins!")
player_one = input("Player One, what is your name? ")
player_two = input("Player Two, what is your name? ")

#function for displaying the game
def display_game() -> None:
    """
        This function displays the boxes for the game
            parameters: N/A
        return: None
    """
    print("")
    for i in range(6):
        print(f"|   {candies[i]}   |", end = '')

#function to tell when game is over
def game_over() -> bool:
    """
        This funciton determines if the game is over
            parameters: N/A
        return: Bool
    """
    for element in candies:
        if element != 0:
            return False
    return True

#the game! yay!
while not game_over():

    display_game()
    #refering to the player by name
    if turn % 2 == 1:
        print(f"\n{player_one}: ", end= '')
    elif turn % 2 == 0:
        print(f"\n{player_two}: ", end= '')

    #selecting the box
    box_selection = False
    while not box_selection:
        box_number = int(input("What box number? "))
        if box_number < 1:
            print("That box does not exist. There are six boxes are labeled 1-6. Select a number between 1-6.")
        elif box_number > 6:
            print("That box does not exist. There are six boxes are labeled 1-6. Select a number between 1-6.")
        elif candies[box_number-1]==0:
            print("That box is empty. Please pick another.")
        else:
            box_selection = True

    #selecting the amount to take
    candy_selection=False
    while not candy_selection:
        candy_number = int(input("How many candies do you want to take? "))
        if candy_number < 1 or candy_number > candies[box_number-1]:
            if candies[box_number-1] == 1:
              print(f"There are only {candies[box_number-1]} candies in Box {box_number}. Select the number 1.")
            else:
                print(f"There are only {candies[box_number-1]} candies in Box {box_number}. Select a number between 1-{candies[box_number-1]}.")
        else:
            candies[box_number - 1] = candies[box_number - 1] - candy_number
            candy_selection = True
    #changing who's next
    turn+=1

#determing the winner
if turn % 2 == 0:
    print(f"Game over! {player_one}, you took the last candy. You win!")
elif turn % 2 == 1:
    print(f"Game over! {player_two}, you took the last candy. You win!")