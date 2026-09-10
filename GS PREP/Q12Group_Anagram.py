# Given an array of strings, group the anagrams together.

# Example
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Expected output can be:

# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]

# The order of the groups and strings doesn't matter.

# Constraints
# 1 <= len(strs) <= 10^4
# 1 <= len(strs[i]) <= 100
# Target

# Aim for O(n × m log m) or better, where:

# n = number of strings
# m = maximum string length
def group_anagrams(strs):
    groups = {}

    for word in strs:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))