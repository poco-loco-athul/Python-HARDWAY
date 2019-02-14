#Ex32: Loops and Lists

elements = []
sum = 0
for i in range(11):
    sum += i
    elements.append(sum)

print("Printing sum of 1 to n, where n is in range(10): ")    
for i in elements:
    print(i, end=" ")

print("\n\nfibonacci series: ")
a,b = 0,1
print(a,b, end=" ")
for i in range(11):
    print(a+b, end=" ")
    temp =a
    a= b
    b= temp +b
print("\n")





