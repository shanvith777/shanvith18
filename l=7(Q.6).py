sentence = input("Enter a sentence: ")

print("\n=====TEXT PROCESSING REPORT=====")

print("original text:", sentence)
print("length:", len(sentence))
print("uppercase:", sentence.upper())
print("lowercase:", sentence.lower())

if len(sentence) > 0:
    print("first character:", sentence[0])
    print("last character:", sentence[-1])

    print("first five characters :", sentence[:5])
    print("reverse text:",sentence[::-1])