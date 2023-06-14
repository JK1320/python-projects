print("Welcome to the quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()

print("Okay, lets play")
score = 0

# question 1
answer = input("What does CPU stands for? ")

if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")


# question 2
answer = input("What does GPU stands for? ")

if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")


# question 3
answer = input("What does RAM stands for? ")

if answer.lower() == "random access memory":
    print("correct!")
    score += 1
else:
    print("Incorrect")



# question 4
answer = input("What does PSU stands for? ")

if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:
    print("Incorrect")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")