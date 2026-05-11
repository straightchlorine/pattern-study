"""
Given a string s and a dictionary of strings wordDict, return true if s can be
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the
segmentation.

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""


def solution_brute(s: str, wordDict: list[str]) -> bool:
    if s == "":
        return True
    for word in wordDict:
        if s.startswith(word) and solution_brute(s[len(word) :], wordDict):
            return True
    return False


from functools import cache


def solution_cache(s: str, wordDict: list[str]) -> bool:
    words = set(wordDict)
    n = len(s)

    @cache
    def f(i):
        if i == n:
            return True

        for word in words:
            if s[i : i + len(word)] == word and f(i + len(word)):
                return True

        return False

    return f(0)


def solution_dp(s: str, wordDict: list[str]) -> bool:
    words = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break

    return dp[n]


if __name__ == "__main__":
    boolean = solution_dp("leetcode", ["leet", "code"])
    print(boolean)
