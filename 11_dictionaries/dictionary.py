# Dictionaries
# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

# For example, a database of phone numbers could be stored using a dictionary like this:

phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781


# Alternatively, a dictionary can be initialized with the same values in the following notation:

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}


# Iterating over dictionaries (using for in)

for name, number in phonebook.iteritems():
	print "Phone number of %s is %d" % (name, number)



# testing code
if "John" in phonebook:
    print "John is listed in the phonebook."


# Removing a value

del phonebook["John"]

# or	phonebook.pop("John")

# conditinal remove

if "John" in phonebook:
	phonebook.pop("John")
	print "Deleted"
