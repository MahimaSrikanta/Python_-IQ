'''
Question 12 : Write a method that takes in a string. Your method should return the
              most common letter in the array, and a count of how many times it appears.
              
complexity Time : O(n)
'''

#Solution I

def most_common_letter(string):
    dict1 = {}
    max_value =0
    for i in string:
        try:
            if dict1[i]:
                dict1[i] = dict1[i] +1

        except:
            dict1.update({i:1})

    for i in dict1.keys():
        if dict1[i] > max_value:
            max_value = dict1[i]
            max_key = i

    return (max_key, max_value)

print("Solution most_common_letter: "+ str(most_common_letter("abbab")))


        
'''
Question 13 : Write a method that takes in a number and returns a string, placing
             a single dash before and after each odd digit. There is one
             exception: don't start or end the string with a dash.

solution : complexity O(n)
'''

#Solution I

def dasherize_number(num):
    str_num = str(num)
    value =[]
    for i in str_num:
        if (int(i)% 2 !=0):
            value.append("-")
            value.append(i)
            value.append("-")
        else:
            value.append(i)
    if value[0]== '-':
        value.pop(0)

    if value[-1]== '-':
        value.pop(-1)

    return "".join (value)

print("Solution most_common_letter: "+ str(dasherize_number(303)))


'''
Question 14 : Write a method that takes in a string of lowercase letters and
           spaces, producing a new string that capitalizes the first letter of each word

'''

#Solution I

def capitalize_words(string):
    list1 = string.split()
    result=[]

    for i in list1:
        value_upper = i.upper()
        result.append(value_upper[0]+ i[1:])

    return " ".join(result)

print("Solution capitalize_words:  "+ str(capitalize_words("this is a sentence")))


'''
Question 15 : Write a method that takes in a string and an array of indices in the
              string. Produce a new string, which contains letters from the input
              string in the order specified by the indices of the array of indices.
'''

#Solution I

def scramble_string(string, positions):
    result = ""
    for i in range(len(string)):
        result = result+ string[positions[i]]

    return result


print("Solution scramble_string:  "+ str(scramble_string("markov", [5, 3, 1, 4, 2, 0] )))

            
    
