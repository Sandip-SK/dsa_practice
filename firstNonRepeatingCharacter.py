def firstNonRepeatingCharacter(word):
    frequency = {}
    for letter in word:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    for i, letter in enumerate(word):
        if frequency[letter] == 1:
            return i
    return -1

# Example usage:
word = "abacabad"
result = firstNonRepeatingCharacter(word)
print(result) 