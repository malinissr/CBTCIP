import random
print("Welcome to Mastermind Game")
print("Player 1 sets number")
Player1=random.randint(1000,9999)
s=0
n=int(input("Guess the number:"))
if(n==Player1):
    print("Player1 guessed the number in 1 try!")
else:
    while(n!=Player1):
        s+=1
        count=0
        n=str(n)
        Player1=str(Player1)
        correct_digit=['Z']*4
        for i in range(4):
            if(n[i]==Player1[i]):
               count += 1
               correct_digit[i] = n[i]
               print(f"The number in the", {i},"index place is correct")
        if(count<4) and (count!=0):
            print(f"Player2 guessed",{count},"digit(s) correctly")
            n=int(input("Enter your next choice:"))
        elif(count==0):
            print("None of the numbers are correct")
            n=int(input("Enter your next choice:"))
print("Player2 guessed all the digits correctly in",s,"tries")
print("\n")
print("Player2 sets the number")
Player2=random.randint(1000,9999)
s1=0
n1=int(input("Guess the number:"))
if(n1==Player2):
    print("Player1 guessed all the digits in 1 try!")
else:
    while (n1 != Player2):
        s1 += 1
        count1 = 0
        n1 = str(n1)
        Player2 = str(Player2)
        correct_digit1 = ['X'] * 4
        for x in range(4):
            if (n1[x] == Player2[x]):
                count1 += 1
                correct_digit1[x] = n1[x]
                print(f"The number in the", {x}, "index place is correct")
        if (count1 < 4) and (count1 != 0):
            print(f"Player1 guessed", {count1}, "digit(s) correctly")
            n1 = int(input("Enter your next choice:"))
        elif (count1 == 0):
            print("None of the numbers are correct")
            n1 = int(input("Enter your next choice:"))
print("Player1 guessed all the digits correctly in",s1,"tries")
print("\n")
if(s>s1):
    print("Hurray!Player2 won the game!")
else:
    print("Hurray!Player1 won the game")









