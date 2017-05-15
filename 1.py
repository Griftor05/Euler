"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

#Should evaluate to 233168

s3 = 3
s5 = 5
nums = []
while s3 < 1000:
    if s3 % 5 != 0:
        nums.append(s3)
    s3 += 3

while s5 < 1000:
    nums.append(s5)
    s5 += 5

sum = 0
for i in nums:
    sum += i

print(sum)