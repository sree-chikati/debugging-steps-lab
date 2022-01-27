"""
Exercise 4
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
    expected output is "" and the actual output is an error
- What error message (if any) is there?
    Error: RecurssionError maximum recursion depth exceeded in comparison
- What line number is causing the error?
    Line number: 40
- What can you deduce about the cause of the error?
    var mid keeps returning 3 and not the intended output
"""

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!
# HINT: It may help to draw a picture to clarify what your assumptions are.

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        # this if statement is also causing an error
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2
    # print(mid)
    # after printing 2 it keeps printing 3 many times and isn't 

    if arr[mid] == element: 
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid)

    else: 
        return binary_search(arr, element, mid, high)
        # this line repeats 995 more times but why?


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)