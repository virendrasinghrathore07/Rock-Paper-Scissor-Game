# Rock Paper Scissor Game 

print("========== Rock Paper Scissor Game ==========")
import random
while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")

    choice = int(input("Enter your Choice : "))


    if choice==1:
        player = "rock"

    elif choice == 2:
        player = "paper"

    elif choice==3:
        player="scissor"

    else:
        print("Invalid Choice")

    computer=random.choice(["rock","paper","scissor"])

    print(f"You chose : {player}")
    print(f"Computer chose : {computer}")

    if player==computer:
        print("Match Tie")

    elif player=="rock" and computer=="scissor":
        print("You Wins !")

    elif player=="rock" and computer=="paper":
            print("Computer Wins !")

    elif player=="scissor" and computer=="paper":
            print("You Wins !")

    elif player=="scissor" and computer=="rock":
            print("You Wins !")

    elif player=="paper" and computer=="scissor":
            print("Computer Wins !")

    elif player=="paper" and computer=="rock":
            print("You Wins !")

    play_again = input("\n Do you want to play again ? (yes/no) --> ").lower()

    if play_again !="yes":
          print("Thanks for playing !!")
          break