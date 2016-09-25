'''
Question 1: Write a method that will take in a number of minutes, and returns a
string that formats the number into `hours:minutes

'''
#Solution I
def time_conversion(minutes):
    hours= minutes//60
    minutes1 = minutes % 60
    

    return (str('{0}:{1:02d}'.format(hours, minutes1)))



print(time_conversion(150))


'''
Question 2: Write a method that takes a string and returns the number of vowels

complexity Time: O(n)
'''

#Solution I
def count_vowels(string):

    check = string.lower()
    count =0
    for i in check:
        if i in "aeiou":
            count= count+1

    return count


print(count_vowels("colour"))


#solution II

def count_vowels1(string):
    check = {'a','e','i','o','u'}
    actual_len = len(string) + len(check)
    for i in string:
        check.add(i)

    result_len =  actual_len -len(check)
    return result_len-1

print(count_vowels1("colour"))


'''
Question 3: Palindrome string
Complexity Time: O(n)
'''

#Solution I

def reverse(word):
    mid= len(word)//2
    end= len(word)-1
    wordlist=[]

    #Convert string into list of strings
    for i in word:
        wordlist.append(i)
    

    #Reverse the strings 
    for i in range(mid):
        temp= wordlist[i]
        wordlist[i] = wordlist[end]
        wordlist[end]= temp
        end= end-1
    if ("".join(wordlist) == word):
        return True
    else:
        return False
       


print("Solution Palindrome: " + str(reverse("a")))


#Solution II

def palindrome(string):
    if string == string[::-1]:
        return True

    else:
        return False

print("Solution Palindrome: " + str(palindrome("abcd")))
    



'''
Question 4: Write a method that takes a string in and returns true if the letter
            "z" appears within three letters **after** an "a".

Complexity Time: O(n)
'''

#Solution I

def nearby_az(string):
    check= string.lower()
    count_a= 0
    count_z=0
    total =0
    for i in range(len(check)):
        if check[i] =='a' and total == 0:
            count_a= i
        elif check[i] =='z' and total == 0:
            count_z= i
            total= total+1

    if((count_z - count_a) == 3):
        return True

    else:
        return False

print("Solution nearby_az : " + str(nearby_az('abz')))
            


'''
Question 5 :Write a method that takes an array of numbers. If a pair of numbers
           in the array sums to zero, return the positions of those two numbers.
           If no pair of numbers sums to zero, return `nil`.

solution : first check if there is any number with negative values, if yes save it and and its index
           Then again check if saved number's positive value is in the array if yes, return both index

complexity Time : O(n)
 
'''

#Solution I

def two_sum(nums):
    result = -1
    index = []
    for i in range(len(nums)):
        if nums[i]<0:
            result *= nums[i]
            index.append(i)

    for i in range(len(nums)):
        if(result == nums[i]):
            index.append(i)
            
    if len(index) > 1:
        return index
    else:
        return "nil"

print("Solution two_sum :" + str(two_sum([1, 3, 5,-3])))



            


        
