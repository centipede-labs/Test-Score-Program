#!/usr/bin/env python3

###########################Version info and welcome
print("Welcome to the Test Score Program V.3.1")
processRunning = 1####Loop for persistence
while processRunning != 0: 
###Reset and Define Variables
    tests = 0
    totalScore = 0
    avg = 0
    base100 = ""
    totalPossible = 0
    margin = 0
    usrInput = ""
    print()
    try:
        tests = int(input("how many test scores?\n"))
    except ValueError:
        if tests >= 1:
            pass
        else:
            print("this has to be a number, please try again")
            continue
    print("=======================")
################Base100 or Special Module
    print("Is this base 100 grading(y) or something special?(n)")
    base100 = input()
    base100 = base100.lower()
    if base100 == 'y':
        for i in range(tests):
            totalScore += int(input("Score?\n"))
            totalPossible += int(100)
    elif base100 == 'n':    
        for i in range(tests):
            totalScore += int(input("Score?\n"))
            totalPossible += int(input("Out of a possible..."))
    else:
        print("Ooops, you did something wrong, please try again")
        continue
#### Calculations
    avg = (totalScore / totalPossible) * 100
    avg = round(avg, 2)
    margin = (totalPossible - totalScore)
#### Reading results
    print ("++++++++++++++++++++++++++++++++++")
    print("your average test score is: " + str(avg)+"%")
    print ("++++++++++++++++++++++++++++++++++")
    print("You scored " + str(totalScore) + " out of a possible " + str(totalPossible))
    if margin == 1:
        print("That means you missed out on " + str(margin) + " point")
    else:
        print("That means you missed out on " + str(margin) + " points")
    print()
    print("In the American grade scale you'd be getting...")
    if avg >=100:
        print("You get an A+ for a beyond perfect score, congratulations! \n All that extra credit paid off!")
    elif avg >=90:
        print("an A overall! Good job!")
    elif avg >=80:
        print("a B overall, not bad!")
    elif avg >=70:
        print("a C overall, you're getting there!")
    elif avg >=60:
        print("a D overall, maybe try a little harder next time?")
    else:
        print("If this were for a standard grade, you'd have failed, I'm sorry.")
########## Repeat process or exit progam
    print()
    print()
    usrInput = input("Would you like to go again?(y/n)")
    usrInput = usrInput.lower()
    if usrInput == "n":
        print("Goodbye, thanks for trying this program.")
        break
