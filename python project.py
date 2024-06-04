import random
num=0
ch = 'y'
while ch.lower() == 'y':
    print("Computer choice is....")
    com = random.choice(["rock","paper","scissor"])
    print(com)
    print("1. Rock\n2. Paper\n3. Scissor")
    user_choice = input("Enter your choice: ")

    if user_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice! Please enter rock, paper, or scissor.")
        continue

    if user_choice == com:
        print("Game is a tie...")
    else:
        if user_choice == "rock" and com == "paper":
            print("COMPUTER WINS")
            print("YOU ARE NOT WIN  \U0001F61E")
        elif user_choice == "paper" and com == "rock":
            print("YOU ARE THE WINNER")
            num += 1
            print("YOUR SCORE:",num)
            print("CONGRATULATIONS  \U0001F603")
        elif user_choice == "rock" and com == "scissor":
            print("YOU ARE THE WINNER")
            num += 1
            print("YOUR SCORE:",num)
            print("CONGRATULATIONS   \U0001F603")
        elif user_choice == "scissor" and com == "rock":
            print("COMPUTER WINS")
            print("YOU ARE NOT WIN \U0001F61E")
        elif user_choice == "paper" and com == "scissor":
            print("COMPUTER WINS")
            print("YOU ARE NOT WIN \U0001F61E")
        elif user_choice == "scissor" and com == "paper":
            print("YOU ARE THE WINNER")
            num += 1
            print("YOUR SCORE:",num)
            print("CONGRATULATIONS   \U0001F603")

    ch = input("Do you want to continue? (y/n): ")

