# Rock paper scissor while keeping the record of the score
import random
userWins = 0
compWins = 0
options = ["rock", "paper",  "scissors"]
while True:
    user_input = input("type Rock/Paper/scissors or press q to quit: ").lower()
    if user_input == 'q':
        break
    if  user_input not in ["rock", "paper",  "scissors"]:
        continue
    randNum = random.randint(0,2)
    computerPick = options[randNum]
    print('computer picked: '+ computerPick+ '.')
    if user_input == 'rock' and computerPick == 'scissors':
        print('you won')
        userWins +=1
    elif user_input == 'paper' and computerPick == 'rock':
        print('you won')
        userWins +=1
    elif user_input == 'scissors' and computerPick == 'paper':
        print('you won')
        userWins +=1
    elif user_input == 'rock' and computerPick == 'rock':
        print('draw')
    elif user_input == 'paper' and computerPick == 'paper':
        print('draw')
    elif user_input == 'scissors' and computerPick == 'scissors':
        print('draw')
    else:
        print("Suck it Loser ! ")
        compWins +=1
    # 0->Rock
    # 1->PApaer
    # 2->Scissors
print (f"your score: {userWins} computer's wins: {compWins}")
print("Goodbye !")
