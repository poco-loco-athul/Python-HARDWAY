#ex23

from sys import argv
script, from_file, to_file = argv


def copy(from_file, to_file):
    open(to_file, 'w').write(open(from_file).read())


copy(from_file, to_file)
print(f"{from_file} copied to {to_file}.")
