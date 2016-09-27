'''
Question: Suppose a sorted array is rotated at some pivot unknown to you beforehand.
          (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).You are given a target value to search.
          If found in the array return its index,otherwise return -1. You may assume no duplicate
          exists in the array.
Solution:

Complexity : O(log n)
'''

def search_binary(array, key):
    left = 0
    right = len(array)-1

    while(left <= right):
        mid= (right+left)//2
        if(array[mid] == key):
            return mid

        #Left side is sorted
        if(array[left]< array[mid]):
            if(array[left]<= key and key< array[mid]):
                right= mid-1

            else:
                left= mid+1


        #Right side is sorted
        else:
            if(array[mid]< key and key<= array[right]):
                left= mid+1

            else:
                right = mid-1

    return -1
            
    
    
    





key = 4
array= [4,5,6,7,0,1,2]

print("The index of target key "+ str(key)+" is found at: "+ str(search_binary(array,key)))
