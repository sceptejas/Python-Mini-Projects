print('welcome to the quiz !!!')
playing = input("Do you want to play ? ")
# print(playing)
# we have used playing.lower to standardise the playing response to lowercase for the in statement 
if playing.lower!='yes': 
    quit()
else :
    print('okay ! The game begins : )')
    print("rules: for eac hright answer you get 1 mark \n for each wrong answer you get -1 mark")
score = 0
answer1 = input("what does CPU stand for? ")
if answer1.lower == "central processing unit":
    print('correct!')
    score = score+1
else:
    print('incorrect !')
    score = score - 1
# question 2
answer2 = input("what does GPU stand for? ")
if answer2.lower == "graphics processing unit":
    print('correct!')
    score = score+1
else:
    print('incorrect !')
    score = score - 1
# question 3
answer3 = input("what does ALU stand for? ")
if answer3.lower == "arithmatic logical unit":
    print('correct!')
    score = score+1
else:
    print('incorrect !')
    score = score - 1
#question 4 
answer4 = input("what language is dominantly used in web developement? ")
if answer4.lower == "javascript":
    print('correct!')
    score = score + 1
else:
    print('incorrect !')
    score = score - 1
# question 5
answer5 = input("is python interpreted or compiled language ? ")
if answer5.lower == "interpreted":
    print('correct!')
    score = score+1
else:
    print('incorrect !')
    score = score - 1


print("your score is ", str(score), "out of 5")
if score>=3:
    print('you have passed the test')
if score == 2:
    print('you are eligibe for a retest')
if score<2:
    print('you should repeat the classes again')
quit()
