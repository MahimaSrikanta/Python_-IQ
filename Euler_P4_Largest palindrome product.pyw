'''
Question4 : A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers

'''

#solution:
def check():
    max_result =0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            result = i*j;
            if(str(result) == str(result)[::-1] and result > max_result):
                 max_result = result
    return(max_result)


print(str(check()))
                
            
            
    
#Solution: 906609

