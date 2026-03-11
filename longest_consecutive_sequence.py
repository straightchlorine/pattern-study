"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:

Input: nums = [1,0,1,2]
Output: 3

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""


def solution(nums: list[int]) -> int:
    """
    Okay, so let's think about it.

    First of all - what is the input and hte Output

    Input is an unsorted array
    Output is the length of the longest consecutive elements sequence

    Easiest approach would be to simply sort and check. But that's not O(n)

    So the approach would be to just keep what we are getting in a hashmap

    But question is what do we store in a hashmap, what do we need to know as we go.
    Answers would be the numbers that we already found and how do those numbers relate.

    For example:
    [100, 4, 200, 1, 3, 2]

    1. 100 - we don't have anything - we write down the <key>:[100]
    (for now no idea what the key would be)
    2. 4 - we check if 100 is +/- 1 = 4 - it is not - another <key>:{100} <key>:{4}
    3. 200 - again - doesn't match none of what we have <key>:[100] <key>: [4] <key>: [200]

    actually that just won't work

    let's come back to the question - what do we need to record in the hashmap

    what do we need to know to say that 4 and 1 (as we go over them) are in the same set
    without knowledge of 3,2 being forward

    the length of the longest consecutive elements sequence

    so how do we build this sequence that we need to get a length of

    how can we build a sequence of consecutive elements without knowlege about the integers

    one way would be to just go over it first - and map it. but then - going over it is already O(n)

    or actually

    as we go over the array - the only thing that we need to know is whether at any point
    there was any number that is either an increment or decrement of the current number

    while writing - we should add anyway - not only if the key doesn't exist
    So when I go to a 100 - i check map[99/101], if key doesn't exist i add the key 100 = True
    when i'm at 4, i check map[3/2] - we don't have that - 4 = True
    when i'm at 200 i check map[199/201] - we don't have that 200 = True
    when i'm at 1 i check map[0/2] - false 1 = True
    when i'm at 3 i check map[2/4] - False/True - 4 is found +2 to length [3,4]
    when i'm at 2 i check map [1,3] - True/True - both are found +2 to length [3,4,1,2]

    That way it isn't sorted and we build the sequence at runtime - let's try implementing

    Okay - here it's a flaw - apparently a set should be used.

    okay so when i'm at 100 my sequence, I check if 99 is there - if not sequence start
    100: 99 in set + 1
    4: 3 in set - previous sequence finishes - save at max_length
    200: 199 in set - false concatenate + 1
    1: 0 in set - false concatenate
    3: 2 in set - true
    """
    sequence = set(nums)
    max_length = 0
    length = 0

    for num in sequence:
        if num - 1 not in sequence:
            current_num = num
            while current_num in sequence:
                length += 1
                current_num += 1

            if length > max_length:
                max_length = length
            length = 0

    return max_length


if __name__ == "__main__":
    print(solution([100, 4, 200, 1, 3, 2]))
    print(solution([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(solution([1, 0, 1, 2]))
