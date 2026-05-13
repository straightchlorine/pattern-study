"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1,
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:

    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
"""

# invariant: characters from s1 match the window in s2
# i.e. char counts in the window match s1's
from collections import Counter


def solution(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    freq = Counter(s1)
    window_freq = Counter(s2[: len(s1)])
    if window_freq == freq:
        return True

    for right in range(len(s1), len(s2)):
        window_freq[s2[right]] += 1
        leaving = s2[right - len(s1)]
        window_freq[leaving] -= 1

        if window_freq[leaving] == 0:
            del window_freq[leaving]
        if window_freq == freq:
            return True

    return False


if __name__ == "__main__":
    print(solution("a", "ab"))
    print(solution("ab", "eidbaooo"))
