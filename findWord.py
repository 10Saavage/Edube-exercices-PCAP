text1 = input("enter a text: ")
text2 = input("enter a text: ")

isOkay = True

for character in text1:
    if character not in text2:
        isOkay = False
        break
    else:
        isOkay = True

if isOkay:
    print("Yes")
else:
    print("No")
