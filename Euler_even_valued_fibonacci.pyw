'''
Question 2: Each new term in the Fibonacci sequence is generated by adding the previous two terms.
            By starting with 1 and 2, the first 10 terms will be:
            By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''



# Solution 
a,b=0,1
result =0
previous=0
while result < 4000000:
    a,b = b,a+b
    if(b % 2==0):
        
        result = result+b

print(result)


# Solution : 4613732


