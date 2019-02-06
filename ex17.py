#ex17 More files

from sys import argv
script, from_file, to_file = argv


print(f"Copying from {from_file} to {to_file}")

indata = open(from_file).read()


print(f"""The inputfile is {len(from_file)} bytes long. 
copying...""")


#outdata=open(to_file, 'w')
#outdata.write(indata)
open(to_file, 'w').write(indata)

print("Done")



#Oneliner:
#open(to_file, 'w').write(open(from_file).read())
#No need to close() here.
#Since it's not saved into a object, it should already be closed by python once that one line runs.

