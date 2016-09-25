'''
Question: Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.

For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.

Solution: Check if both words are of equal length and then create set1 and set2 out of word1 and word2 respectively and return TRUE or FALSE
based on length of each set
corner case: abcd , efdd


Complexity Time : O(n)
'''

def Isomorphic():
    word1= input("Enter the first word: ")
    word2= input("Enter the second word: ")
    
    #check if both words of equal length or not
    if len(word1) == len(word2):
        set1= set()
        set2= set()
        
        #Create set1 out of word1, to remove any repetion 
        for letter in word1:
                       
            set1.add(letter)
        
        #Create set2 out of word2, to remove any repetion 
        for letter in word2:
            set2.add(letter)
        
        #Check now if length of both sets are equal or not , if equal then return True else False
        if len(set1) == len(set2):
            
           return True
                       
        else:
            return False
        

    else:
       return False

    
result = Isomorphic()
print(result)

