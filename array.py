
"""
Reverse array in place:
i.e without creating a new dataStructure to hold the array in place ...
write a function reverseArray(A) that takes in an Array A and reverse it, without using another array in place
A = [20, 10, 6, 8]
"""
"""defined a function that takes in a parameter"""

def reverseArray(A):
    """ logic of the variables that keeps track of the indices you need to track"""
    start = 0
    stop = len(A) 
    """looping through the items, in this case while loop will make sense when the condition is false"""
    while start < stop:
        """swapping the items using tuple assignment  """
        A[start],A[stop - 1 ] = A[stop - 1 ],A[start]
        """incrementing the counter """
        start += 1
        stop -+ 1
    return A 
print(reverseArray(A = [1, 2, 3, 4]))



    



