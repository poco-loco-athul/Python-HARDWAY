#Ex39: Dictionaries, oh Lovely Dicitonaries

stuff = { 'name' : 'Athul', 'age' : 23 , 'town' : 'Calicut' }
print('stuff =',stuff)

print("Adding more items to stuff..")
stuff[1] = "Wow"
stuff[2] = "Where this goes"
print(stuff)

print("Deleting those items from stuff")
del stuff[1], stuff[2]
print(stuff)


# connecting two dicts!

dictA = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
print("\ndictA = ", dictA)
dictB = { 1 : 'one', 3 : 'three', 5 : 'five' }
print("dictB = ", dictB)


print("dictB[dictA['c']] =",dictB[dictA['c']])
print("dictB[dictA['e']] =",dictB[dictA['e']])

print("\ndict.get(key): ")
print('dictB.get(1) =',dictB.get(1))

# from collections, collections.OrderedDict is a data structure which will remember insertion order, unlike regular dict

#   len(dict)           - return number of items in dict
#   dict[key]           - return item of dict with key 'key'
#   get(key)            - returns value for key if exists
#   items()             - returns items of dict in (key, value) pairs
#   keys()              - returns keys of dict
#   values()            - returns values of dict
#   dict[key] = value   - set dict[key] to value

#   fromkeys(seq)       - creates new dict with keys from seq and sets values to None
#   del dict[key]       - remove dict[key] from dict
#   clear()             - removes all items in dict
#   copy()              - returns shallow copy of dict
#   pop(key)            - remove and return value of key
#   popitem()           - remove and return random (key, value) pair of dict
#   setdefault(key)     - return key's value if exists, else insert key with value None
#   update([other])     - overwrite existing keys with values from other

#   key in dict         - True if dict has key 'key'
#   key not in dict     - True if dict has no key 'key'
#   iter(dict)          - returns iterator over the keys of dict


