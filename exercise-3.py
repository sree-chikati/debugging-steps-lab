"""
Exercise 3
"""

# PART 1: Gather Information
#
# TODO: Gather information about the source of the error and paste your findings here. E.g.:
# - What is the expected vs. the actual output?
# - What error message (if any) is there?
# - What line number is causing the error?
# - What can you deduce about the cause of the error?

"""
Part 1: 
- What is the expected vs. the actual output?
    expected output is "[1, 2, 3, 5, 6]" and the actual output is an error
- What error message (if any) is there?
    Error: list index out of range
- What line number is causing the error?
    Line number: 40
- What can you deduce about the cause of the error?
    The cause of the error is that var j loops through an index that does not exist
"""

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    # for loop sets range from 1 to the length of
    for i in range(1, len(arr)):
        key = arr[i] 
        # j is being set to something
        j = i-1
        while key < arr[j] : 
            arr[j+1] = arr[j] 
            # j is being reassigned to something anf this won't work 
            # because of the while loop
            j -= 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

