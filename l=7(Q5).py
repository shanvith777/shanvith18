text = input("enter a sentence: ")

word = input("enter a word to search: ")

print("uppercase:", text.upper())
print("lowercase:", text.lower())

print("number of times word occurs:", text.count(word))

if word in text:
    print("The word is present in the sentence.")
else:
    print("the word does not exist in the sentence.")

    old_word = input("enter a word to replace: ")
    new_word = input("enter a new word: ")

    new_text = text.replace(old_word, new_word)

    print("modified sentence:", new_text)