# Dictionaries are the Python's version of
# hash tables ( they allow as to create a "mapping"
# with key:value pairs)

dict = {"key":"value", 'key1':1, 2:True,"key2":{'k':[1,2,"GrabMe"]}}
print(dict["key2"]['k'][2].upper())

#add new key-value
dict['newKey'] = 'newValue'
print(dict)
