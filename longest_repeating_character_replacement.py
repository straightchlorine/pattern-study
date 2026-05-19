"""
You are given a string s and an integer k. You can choose any character of the
string and change it to any other uppercase English character.

You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:

    1 <= s.length <= 105
    s consists of only uppercase English letters.
    0 <= k <= s.length
"""

# invariant: window contains at most k characters that are not the most frequent
# character in the window
from collections import defaultdict


def solution(s: str, k: int) -> int:
    count = defaultdict(int)
    left = 0
    max_freq = 0
    result = 0
    for right in range(len(s)):
        # count current character (will also add in case invariant holds)
        count[s[right]] += 1
        # get the highest frequency within the window
        max_freq = max(max_freq, count[s[right]])

        # size of the sliding window
        size = right - left + 1
        if size - max_freq > k:
            # in case invariant breaks
            count[s[left]] -= 1  # remove this one character from the count
            left += 1  # shrink the window
            continue

        result = max(size, result)

    return result  # since it doesn't count when left==right==0


if __name__ == "__main__":
    solution("ABAB", 2)  # 4
