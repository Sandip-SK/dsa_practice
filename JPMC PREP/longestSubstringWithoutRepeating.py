# Longest Substring Without Repeating Characters
# Given a string s, return the length of the longest substring without repeating characters.
# Examples
# s = "abcabcbb"
# Output = 3

# Because:
# "abc"

# is the longest substring without duplicates.
# Another:
# s = "bbbbb"
# Output = 1

# And:
# s = "pwwkew"
# Output = 3

# because "wke" has length 3.
def longest_substring(s):
    seen = set()
    left = 0
    res = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        res = max(res, right - left + 1)

    return res