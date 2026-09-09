# Problem 2 — Sliding Window

# Given a string s, find the length of the longest substring without repeating characters.

# Examples
# Input:  "abcabcbb"
# Output: 3

# Explanation: "abc" is the longest substring without repeating characters.

# Input:  "bbbbb"
# Output: 1
# Input:  "pwwkew"
# Output: 3

# Explanation: "wke" is the longest substring without repeating characters.

# Constraints
# 0 <= len(s) <= 5 * 10^4

# Try to solve it in O(n) time.

def longest_substring(s):
    left = 0
    res = 0
    seen = set()
    for right in range(len(s)):
        if s[right] in seen:
            
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
        seen.add(s[right])        
        res = max(res, right - left + 1)
    return res