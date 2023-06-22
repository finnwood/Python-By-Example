# Pig Latin Converter
wordIn = str(input("Please enter a word to be converted into pig latin "))
first = wordIn[0]
length = len(wordIn)
rest = wordIn[1:length]
if first.lower == "a" or "e" or "i" or "o" or "u":
    newWord = rest+first+"way"
else:
    newWord = rest+first+"ay"
print(newWord)