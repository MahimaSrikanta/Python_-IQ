'''
Question : Write a method that takes in a string of lowercase letters (no
           uppercase letters, no repeats). Consider the *substrings* of the
           string: consecutive sequences of letters contained inside the string.
           Find the longest such string of letters that is a palindrome.

Solution : Using Matrix
Complexity Time : O(n^2)
'''

#Solution I
import numpy

def Longest_palindrome(string):
    length = len(string)
    palindrome_begin = 0
    max_len = 1
    #2d Matrix with false values filled
    palindrome= numpy.full((length,length), False, dtype=bool)
    

    #single character
    for i in range (length):
        palindrome[i][i] = True
    

    #Two characters
    for i in range (length-1):
        if string[i] == string[i+1]:
            palindrome[i][i+1] = True
            palindrome_begin = i
            max_len = 2
    

    #Three or more characters
    for i in range(3,length):
        for j in range(length-i+1):
            k= j+i-1
            if(string[j] == string[k] and  palindrome[j+1][k-1]):
                palindrome[i][j] = True
                palindrome_begin = i
                max_len = i
    print(palindrome)
    return string[palindrome_begin: max_len+ palindrome_begin]

print(Longest_palindrome('banana'))

