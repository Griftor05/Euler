"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# Should eval to 6857

myInt = 600851475143
print(myInt)

# Going to Sieve it, cause I think that should be faster
counter = 1
primesList = []
largest = 3

# Going to start at a logical place - myInt / 2 + 1, then move backwards from there, checking the primality of each number
# I drop to. I do know that each prime number is only one away from a multiple of 6, so I can make it easier in that way.
myStart = myInt / 2
myStart += 1

