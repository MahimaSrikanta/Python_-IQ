'''
Question:  Write a method that takes an integer `n` in; it should return
           n*(n-1)*(n-2)*...*2*1. Assume n >= 0.

Solution I: Using Recursion
Solution II: Recursion with memoization
Solution III: Loops


'''


#Solution I (Recursion)

def factorial_a(num):
    if num == 1:
        return 1

    return num * factorial_a(num-1)


print(factorial_a(5))



#Solution II (Recursion with memoization)

def factorial_b(num,dict1):
    
    if num == 1:
        return 1
    try:
        if dict1[num]:
            return dict1[num]
    except:
        dict1[num] = num*factorial_b(num-1,dict1)
        return dict1[num]

d1= {}
print(factorial_b(7,d1))




#Solution III(Loop)

def factorial_c(num):
    if num < 0:
        return 0
    result = 1
    
    while num >0:
        result *= num
        num = num-1

    return result


print(factorial_c(7))
    

    
    
