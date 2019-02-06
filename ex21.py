#ex21 Functions can return something

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multi(a,b):
    return a * b


x=int(input("Enter a number: "))
y=int(input("Enter another number: "))


print(f"""
Sum of these numbers is {add(x,y)}
Difference between these numbers is {sub(x,y)}
Product of these numbers is {multi(x,y)}
""")

