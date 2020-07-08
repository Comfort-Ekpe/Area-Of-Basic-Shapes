# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

'''
Project evaluation
-> Take the value of the integer and store in a variable.
-> Using a while loop, first obtain the factors of the number.
-> Using another while loop within the previous one, compute if the factors are prime or not.
-> Exit.

'''
v = []
n = 600851475143
i = 2
while i * i < n:
     while n % i == 0:
         n = n / i
     i = i + 1
# print (n)
# v.append(n)
# v.sort()
# print("The largest number among the factors of 600851475143 is:", v)



# QUESTION FOUR
'''
The sum of the squares of the first ten natural numbers is,

12+22+...+102=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)2=552=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import functools
# from math import fsum
sumn= []
sqsum = []
i = 1
for i in range(2, 101):
	v = i ** 2
	sumn.append(v)	
print("The sum of the squares of the first 100 natural numbers are", functools.reduce(lambda a,b : a + b, sumn))
for i in range(2, 101):
	sqsum.append(i)
	print(sqsum ** 2)
print(functools.reduce(operator.mul,))
