word = "banana"

freq = {}

for letter in word:
    if letter in freq:
        freq[letter] += 1
    else:
        freq[letter] = 1

print(freq)

