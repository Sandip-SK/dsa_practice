# First Unique Character in a String

# Given a string s, return the first character that appears exactly once.

# If no such character exists, return None.

# Examples:

# s = "leetcode"
# → "l"
# s = "loveleetcode"
# → "v"
# s = "aabbcc"
# → None

# Constraints:

# 0 <= len(s) <= 10^5

# Target: O(n) time.
def first_unique_char(s):
    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in s:
        if counts[char] == 1:
            return char

    return None