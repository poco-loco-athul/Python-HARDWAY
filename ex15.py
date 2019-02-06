#ex15 Reading files

from sys import argv
script, filename = argv


txt = open(filename)

print("Here is the filename:", filename)
print(txt.read())

txt.close()
