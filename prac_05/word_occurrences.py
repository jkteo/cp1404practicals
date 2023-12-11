"""
Word Occurrences
Estimate: 20 minutes
Actual:   40 minutes
"""

words = {}
sentence = input("Please enter a sentence: ").split()
sentence.sort()

for word in sentence:
    try:
        words[word] += 1
    except KeyError:
        words[word] = 1

max_length_word = max(len(word) for word in list(words.keys()))

for word, count in words.items():
    print(f"{word:{max_length_word}} : {count}")
