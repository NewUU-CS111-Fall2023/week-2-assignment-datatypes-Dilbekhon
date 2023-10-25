"""
 Author: Dilbekkhon
 Date: 25-10-2023
 Name: String matching
"""

def find_match(sentence, word):
    sentence_lower = sentence.lower()
    word_lower = word.lower()

    index = sentence_lower.find(word_lower)

    if index != -1:
        print(f"Match found at index {index}")
        return True
    else:
        print("No match")
        return False

sentence = input("Enter a sentence: ")
word = input("Enter a word to match: ")

result = find_match(sentence, word)
print("Result:", result)
