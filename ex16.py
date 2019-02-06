#ex16 Reading and writing files

from sys import argv
script, filename = argv

target = open(filename, 'w')
# 'w' for writing permission

print("Opening the file..\nGive inputs")

line1 = input("line1: ")
line2 = input("line2: ")

print("Writing", filename)

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
target.write(line1+ "\n"+ line2+ "\n")

print("Done")
target.close()

# Why should I close() the file object?
# First, Python does not promise that it will close the files for you. The operating system does, when the program exits.
# If your program does something else for a while, or repeats this sequence of steps dozens of times, you could run out of resources, or overwrite something.



