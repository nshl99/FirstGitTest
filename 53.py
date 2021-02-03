# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:03:25 2020

@au"thor: Nishil
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



def binomial(n,r):
    return (factorial(n)/(factorial(r)*factorial(n-r)))


r = 0
nums = 0
i = 0
while True:
    n = 100 - i
    while r <= n//2:
        if binomial(n,r) <= 1000000:
            r += 1
        else:
            nums += (n-r)-(r-1)
            break
    i += 1
    if r > n//2:
        break
end = timer()

print(nums)
print(end-start)


    


            
            
            
            