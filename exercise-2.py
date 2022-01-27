"""
Exercise 2
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
    expected output is "false true" and the actual output is "false false"
- What error message (if any) is there?
    Error: No error
- What line number is causing the error?
    Line number: 36 and 44
- What can you deduce about the cause of the error?
    The error occurs when you return True of False and this is because 
    the function return those values without finishing the for loop
"""


# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    # for i in the range of length var list_of_nums minus 2...
    for i in range(len(list_of_nums) - 2):
        # if statement is compiling and doing the work
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True
        else:
            # The following print statement proves the error because it prints 4 1 2 and 
            # not the intended output because it doesn't iterate through the for loop one last time
            # print(list_of_nums[i], list_of_nums[i+1], list_of_nums[i+2])
            return False

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True