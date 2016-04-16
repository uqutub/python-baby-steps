# http://www.learnpython.org/en/Loops
# Loops

# "for" loop

# For loops iterate over a given sequence. Here is an example:
primes = [2, 3, 5, 7]
for prime in primes:
    print prime


# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions. The difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, which is more efficient.

# Prints out the numbers 0,1,2,3,4
for x in xrange(5): # or range(5)
    print x

# Prints out 3,4,5
for x in xrange(3, 6): # or range(3, 6)
    print x

# Prints out 3,5,7
for x in xrange(3, 8, 2): # or range(3, 8, 2)
    print x



# "while" loops

# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print count
    count += 1  # This is the same as count = count + 1



# "break" and "continue" statements
# break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the "for" or "while" statement. A few examples:

# Prints out 0,1,2,3,4
count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in xrange(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print x



# can we use "else" clause for loops?
# unlike languages like C,CPP.. we can use else for loops. When the loop condition of "for" or "while" statement fails then code part in "else" is executed. If break statement is executed inside for loop then the "else" part is skipped. Note that "else" part is executed even if there is a continue statement.

# Here are a few examples:

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print count
    count +=1
else:
    print "count value reached %d" %(count)

# Prints out 1,2,3,4
for i in xrange(1,10):
    if(i%5==0):
        break
    print i
else:
    print "this is not printed because for loop is terminated because of break but not due to fail in condition"
