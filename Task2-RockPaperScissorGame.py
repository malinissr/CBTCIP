'''ROCK PAPER SCISSOR GAME
Winning rules:
Rock vs Paper->Paper wins
Rock vs Scissor->Rock wins
paper vs Scissor->scissor wins'''




import random

print("Winning Rules of the game:\nRock vs paper->Paper wins\n"
      "Rock vs scissor->Rock wins\n"
      "Paper vs scissor-> scissor wins\n")
choice=int(input("Enter your choice:\n1.Rock\n2.Paper\n3.Scissor\n"))
while(choice>3 or choice<1):
    choice=int(input("Enter a valid choice:"))
while(choice<=3):
    if(choice==1):
        user_choice="Rock"
    elif(choice==2):
        user_choice="Paper"
    else:
        user_choice="Scissor"
    print("\n")
    print("User choice is",user_choice)
    print("\n")
    print("\n")
    print("Its computer turn")
    print("\n")
    computer_choice=random.randint(1,3)

    while computer_choice==choice:
        computer_choice=random.randint(1,3)
    if computer_choice==1:
        comp_choice='Rock'
    elif computer_choice==2:
        comp_choice='Paper'
    else:
        comp_choice='Scissor'
    print("Computer choice is",comp_choice)
    print(user_choice,"vs",comp_choice)

    if choice==computer_choice:
        print("Its draw\n")
        result="DRAW"


    if(choice==1 and computer_choice==2):
        print("Paper wins\n")
        result="Paper"
    elif(choice==2 and computer_choice==1):
        print("Paper wins\n")
        result="Paper"


    if(choice==1 and computer_choice==3):
        print("Rock wins\n")
        result="Rock"
    elif(choice==3 and computer_choice==1):
        print("Rock wins\n")
        result="Rock"


    if(choice==2 and computer_choice==3):
        print("Scissor wins\n")
        result="Scissor"
    elif(choice==3 and computer_choice==2):
        print("Scissor wins\n")
        result="Scissor"

    if(result==user_choice):
        print("--------------------Hurray!USER WINS-----------------------")
    else:
        print("--------------------Hurray!COMPUTER WINS-------------------")
    break

print("Thanks for playing!")

