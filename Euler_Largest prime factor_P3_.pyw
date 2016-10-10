'''
Question: The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Solution: The largest prime factor can never be greater than sqrt of the number.
Hence the other loop makes sure of this condition. The inner loop states that while i divides evenly into n, replace n with n divided by i.
This loop runs continuously until it is no longer true

'''

#Solution
def prime_factor(n):
    
    result =2
    while result * result < n:
        while n%result ==0:
            n= n/ result

        result= result+1

    return n


print(str(prime_factor(n= 600851475143)))
        
#Soution: 6857        
