#!/usr/bin/python3

# 99 beers on the wall
# From r/beginnerprojects
# http://bit.ly/29NuVIW

x = 99

while x >= 1:
    if x == 1:
        print (str(x) + " bottle of beer on the wall, " + str(x) + " bottle of beer.")
    else:
        print (str(x) + " bottles of beer on the wall, " + str(x) + " bottles of beer.")
    x = x - 1
    print ("Take one down, pass it around, " + str(x) + " bottles of beer on the wall.")
    print(" ")

print ("No more bottles of beer on the wall, no more bottles of beer.")
print ("Go to the store, by some more, 99 bottles of beer on the wall.")
