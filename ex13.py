#ex13 Parameters, Unpacking, Variables


from sys import argv
# import is an option add libraries(modules) to your script
#print(argv)

script, first, second, third = argv

print("The script is called:",script)
print("first variable is:", first)
print("second variable is ", second)
print("third variable is:", third)

