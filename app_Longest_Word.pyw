'''
Question: Write a method that takes in a string. Return the longest word in
the string. You may assume that the string contains only letters and spaces

Solution: Split the string into words based on space and check for the longest word

'''


def Logest_word(sentence):
    result= sentence.split(" ")
    max_len = 0
    for i in result:
        
        if len(i) > max_len:
            max_len= len(i)
            max_word = i

    return max_word

print(Logest_word("Helloooooooo this is Mahimma"))

            
            
