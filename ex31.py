#Ex31: Making Decisions

print("""I have chosen a range of 3 numbers between 1 to 10
Can you guess any of the number in this range?
What is your guess?""")

guess=int(input(">"))

if guess == 7:
    print("You are too sharp. You just found the middle number from chosen range")
elif guess in range(6,9):
    print("You are right. Try again to find other numbers")
else:
    print("Try again")
    
