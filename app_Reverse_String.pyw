'''
Question : Write a method that will take a string as input, and return a new
string with the same letters in reverse order.

solution I: 
Solution II:Convert the string into list of string and take pointer till midpoint and reverse the string list

complexity Time: O(n)

'''

#Solution I



#Solution II
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
    return("".join(wordlist))
       


print(reverse("mahi"))
    
    
