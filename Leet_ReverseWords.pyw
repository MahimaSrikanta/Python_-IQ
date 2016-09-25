'''
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".


Solution I : Use Python's reversed or [::-1]
Solution II : Saving the indexes of spaces and reversing the string based on those saved indexes

Complexity Time : O(n)
'''

#Solution I

s= ("Hi this is Mahima")
r= " ". join(reversed(s.split()))
print(r)


s = ("Hi this is Mahima")
r= " ". join(s.split()[::-1])
print(r)




#Solution II
def reverse(index,s):
    l= []
    count = len(index)-1
    while count >0:
        i= index[count-1]
        l.append(s[i: index[count]])
        count = count-1
        
    
    print("".join(l))



def leet(s):
    index = [0]
    for i in range(0,len(s)):
        if (s[i] == " "):
            index.append(i+1)
    index.append(len(s))
    reverse(index,s)

   

leet("Hi this is Mahima")
            
