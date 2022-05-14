text1 = list('listen')
text2 = list('silent')
anagram = True

if len(text1) == len(text2):
    for character in list(text1):
        if character not in list(text2):
            anagram = False
            break
else:
    anagram = False

if anagram:
    print("Anagram")
else:
    print("Not Anagrams")
