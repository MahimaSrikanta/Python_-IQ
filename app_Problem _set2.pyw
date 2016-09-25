'''
Question 10: Write a method that takes in a number and returns true if it is a
power of 2. Otherwise, return false.

'''

#Solution I
def is_power_of_two(num):
    if num %2 != 0:
        return False
    power =0
    result = 2** power
    
    while result <= num:
        if result == num:
            return True
            
        power = power+1
        result = 2**power
        

    return False


print("Solution is_power_of_two: " + str(is_power_of_two(0)))


#Solution II
def power_of_two(num):
    if num < 1:
        return False

    while True:
        if num == 1:
            return True

        elif num %2 == 0:
            num = num/2

        else:
            return False


print("Solution is_power_of_two: " + str(power_of_two(16)))


'''
 Question 11: Write a method that takes an array of numbers in. Your method should
             return the third greatest number in the array. You may assume that
             the array has at least three numbers in it.
'''

#Solution I

def third_greatest(nums):
    
    
    x = 3;
    while x > 0:
        max_num = 0
        for i in nums:
            if i > max_num:
                max_num = i

        nums.remove(max_num)
        x= x-1
    return max_num

print("Solution third_greatest: " + str(third_greatest([2, 3, 7, 4])))


#Solution II

def third_greatest1(nums):
    first =0
    sec=0
    third =0
    
    for i in nums:
        if i> first:
            third = sec
            sec = first
            first = i
            
        elif i> sec:
            third = sec
            sec =i
            
        elif i> third:
            third = i

    return third

print("Solution third_greatest: " + str(third_greatest1([0,0,10,4,6])))
        
    




        


    
