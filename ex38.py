#Ex38: Doing Things to Lists

ten_things = "apples oranges ladder rat mike bike cake food pizz fuel"
stuff = ten_things.split(" ")

more_stuff = ["python", "snake", "Girl", "boy"]

print(stuff)
print("appending",end="")
while len(stuff) != 14:
    next_item = more_stuff.pop()
    stuff.append(next_item)
    print(".",end="")
print("\n")
print(stuff)    

    

