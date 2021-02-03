# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:25:26 2020

@author: Nishil
"""
from timeit import default_timer as timer
start = timer()

def factorial(number):

    prime = [True]*(number + 1)
    result = 1
    for i in range (2, number+1):
        if prime[i]:
            #update prime table
            j = i+i
            while j <= number:
                prime[j] = False
                j += i
            sum = 0
            t = i
            while t <= number:
                sum += number//t
                t *= i
            result *= i**sum
    return result



def binomial_squared(r):
    return (factorial(20)/(factorial(r)*factorial(20-r)))**2

print(sum(map(binomial_squared,list(range(0,21)))))
end = timer()

"""tracks = 0
for i in range(0,21):
    tracks += (binomial(20,i))**2"""

print(end-start)