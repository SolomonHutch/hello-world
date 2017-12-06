import random
import time

answer = random.randint(1, 6)
answer1 = random.randint(1, 3)
answer2 = random.randint(1, 1000)
# sets random values

ans = "Yes"

name = input("what is your name?\n")

if answer1 == 1:
    print("I see that...")

elif answer1 == 2:
    print("the future holds this:")

else:
    print("I shall now enlighten you...")

while ans == "Yes" or ans == "yes":

    answer = random.randint(1, 6)
    answer1 = random.randint(1, 3)
    answer2 = random.randint(1, 1000)
    # sets random values

    if name == "Isaac" or name == "Nicholas":  # ditermines awnser options
        if answer == 1:
            if answer == 1:
                print("You will see someone you have never seen before this week")

            elif answer == 2:
                print("You will do reasonably well in your GCSEs")

            elif answer == 3:
                print("You will find something you lost this year")

            elif answer == 4:
                print("You will trip in the next 11 years")

            elif answer == 5:
                print("You will wear some pants in the next 37 years")

            else:
                print("You will die in the next 2000 years")
        else:
            print("you will never have a girlfrend, ever.")

    elif name == "Solomon" or name == "solomon" or name == "Kori":  # ditermines awnser options
        if answer1 == 1:
            print("you will always be amazing")

        elif answer1 == 2:
            print("you will remain super brilliant")

        else:
            print("you will always be the most awesome person ever")

    elif name == "Mr Asoah":
        print("someone peed in your cup.")

    elif name == "Mr Cool" or name == "Megamind":
        print("that is not your true name...\n")
        time.sleep(2)
        print("...and i sense it is the opposite of the truth!")
        exit()

    elif name == "Jack":  # ditermines awnser options
        if answer1 == 1:
            print("you will enjoy doing computer science!")

        elif answer1 == 2:
            print("you have an amazing frend.")

        else:
            print("you are not sad, alone and overweight(sleeping in your mom's basement)")

    elif name == "David":
        print("you will procede to smell bad forever!!")

    else:  # ditermines awnser options
        if answer == 1:
            print("You will see someone you have never seen before this week")

        elif answer == 2:
            print("You will do reasonably well in your GCSEs")

        elif answer == 3:
            print("You will find something you lost this year")

        elif answer == 4:
            print("You will trip in the next 11 years")

        elif answer == 5:
            print("You will wear some pants in the next 37 years")

        else:
            print("You will die in the next 2000 years")

    ans = input("\nWould you like another fortune? No / Yes\n  ")
    # ditermines if loop will end

    if ans == "No" or ans == "no":
        print("Goodbye.")
    elif ans == "Yes" or ans == "yes":  # ditermines future seeing awnser
        if answer1 == 1:
            print("I see that...")

        elif answer1 == 2:
            print("the future holds this:")

        else:
            print("I shall now enlighten you...")



    else:
        print()
