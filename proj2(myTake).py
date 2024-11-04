import random
r = random.randint(-5,10)
print(r)
tries = 1
print('the number lies between -5 and 10')
print('you will get 8 tries to guess the number')
while tries <=8:
    guess = int(input("your guess? "))
    if guess != r:
        tries += 1
    if guess == r:
        print(f'correct guess, you took {tries} tries')
        quit()
    else:
        print('try again')
        continue
print("too many tries: you lost !")
