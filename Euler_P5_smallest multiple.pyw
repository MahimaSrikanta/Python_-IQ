'''
Question 5: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution: hat you want is the least common multiple of 11 through 2020. This can be computed recursively as:
    lcm(1,2,…,20)=lcm(lcm(1,2),3,…,20)=⋯
    lcm(1,2,…,20)=lcm(lcm(1,2),3,…,20)=⋯
    or can also be computed by factoring all the numbers 11 through 2020 to find the highest degree on each prime from 11 to 2020 in any factor.
    The primes between 11 and 2020 are 2,3,5,7,11,13,17,192,3,5,7,11,13,17,19. The highest exponent on 22 in any prime factorization of a number
    between 11 and 2020 is 44, as 24=1624=16 but 25=32>2025=32>20. For 33 it is 22, and for all higher primes it is 11. Thus we have
    lcm(1,2,…,20)=24⋅32⋅5⋅7⋅11⋅13⋅17⋅19.

'''

#Solution:

import math
def smallest_mutiple(n):
    primes = [2]
    count =3
    #Program to get all the prime numbers between 2 to n and puts into list primes
    while count <= n:
        isprime = True
        
        for x in range(2, int(math.sqrt(count)+1)):
            if(count % x ==0):
                isprime = False;
                break
        if(isprime):
            primes.append(count)
        count=count+1

    smallest_number =1

    #below program checks for the highest exponents of the listed prime numbers whose after calculation of exponent value is within n
    #and product of it.
    for i in primes:
        power =1
        while(i** power < n):
            power = power+1
        smallest_number = smallest_number*(i**(power-1))    
            
                

    return (smallest_number)


print(str(smallest_mutiple(20)))


#Solution: 232792560

            
            
           
           
           
           
        
