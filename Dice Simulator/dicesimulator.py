'''
Dice Simulator is an interesting game that can be played between two peoples. Both people have to simulate the dice
again and again to reach the target value decide by the people itself and the person who hit the target value first
will win the game.
'''

import random


def start(player_name, comp_score, user_score, target):
    print("Let's start the game".center(200, "-"))
    chances = 0
    while True:
        chances += 1
        comp_dice_simulate = random.randint(1, 6)
        comp_score += comp_dice_simulate
        user = input("Press enter key to simulate the dice.\n")
        user_dice_simulate = random.randint(1, 6)
        print(f"Computer Dice Number is {comp_dice_simulate}")
        print(f"{player_name} Dice Number is {user_dice_simulate}")
        user_score += user_dice_simulate
        if comp_score > target:
            comp_score -= comp_dice_simulate
        if user_score > target:
            user_score -= user_dice_simulate
        print(f"Computer Current Score is {comp_score}")
        print(f"{player_name} Current Score is {user_score}")
        print("".center(30, "|"))
        if comp_score==target and user_score==target:
            print("Both players are winner of this game...")
            break
        elif comp_score==target:
            print(f"Computer won this game in {chances} chances.")
            break
        elif user_score==target:
            print(f"{player_name} won this game in {chances} chances.")
            break
        else:
            pass


if __name__ == '__main__':
    s = set()
    print("Welcome To The Dice Simulator Game".center(150, "-"))
    while True:
        player_name = input("Enter your name here:\n")
        if player_name in s:
            print(f"Hi, {player_name}")
            target_by_user = int(input("Enter the one target value here:\n"))
            comp_score, user_score, target = 0, 0, target_by_user
            start(player_name, comp_score, user_score, target)
        else:
            s.add(player_name)
            print("Your name is not present in our list. But don't worry, we are adding your name now\n")
            continue

        inp = input("Press c to continue and q to quit:\n")
        if inp=="c":
            continue
        else:
            quit()