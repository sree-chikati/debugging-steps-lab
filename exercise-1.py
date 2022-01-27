"""
Exercise 1
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
    expected output is 4 and the actual output is error
- What error message (if any) is there?
    Error: Out of range
- What line number is causing the error?
    Line number: 39
- What can you deduce about the cause of the error?
    In the for loop's last iteration, specifically listOfNums[i+1] is out of bounds
"""

# PART 2: State Assumptions
#
# TODO: State your assumptions here or say them out loud to your partner ...
# Make sure to be SPECIFIC about what each of your assumptions is!

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    # largest_diff var set to 0
    largest_diff = 0
    # for i in rage length of para list_of_nums
    for i in range(len(list_of_nums)):
        # new var diff set to abs of...
        # cannot set i in list_of_nums
        # check is abs func is being used correctly
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        # if diff is greater than largest_diff... so if abs value of the above is greater
        if diff > largest_diff:
            # largest_diff set to diff
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)