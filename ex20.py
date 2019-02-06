#ex20 Functions and Files

from sys import argv
script, from_file, to_file = argv


def copy(from_file, to_file):
    open(to_file, 'w').write(open(from_file).read())


copy(from_file, to_file)
print(f"{from_file} copied to {to_file}.")

# Using concepts from ex17, made a copy function.
