import random

if __name__ == '__main__':
    print("Welcome To The Rock | Paper | Scissor Game".center(150, "-"))
    print("Choose:\nr for Rock\np for Paper\ns For Scissor")
    tie = 0
    total_chances = 10
    user_score = 0
    comp_score = 0
    while total_chances > 0:
        total_chances -= 1
        comp_choice = random.choice(["r", "p", "s"])
        user = input("Enter your input here:\n").lower()
        if user=="r" and comp_choice=="s" or user=="p" and comp_choice=="r" or user=="s" and comp_choice=="p":
            print("You won this chance")
            user_score += 1
        elif user=="r" and comp_choice=="p" or user=="p" and comp_choice=="s" or user=="s" and comp_choice=="r":
            print("Computer won this chance")
            comp_score += 1
        else:
            print("There is a tie...")
            tie += 1
    print(''.center(100,"-"))
    print(f"Total Tie score = {tie}")
    print(f"Computer total score = {comp_score}")
    print(f"User total score = {user_score}")
    if comp_score > user_score:
        print(f"Computer won this game with the score of {comp_score-user_score}.")
    elif user_score > comp_score:
        print(f"You won this game with the score of {user_score-comp_score}.")
    else:
        print("There is a tie.")

