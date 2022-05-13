message = input("enter a text: ").lower()
message = message.replace(' ', '')
if message == '':
    print("it's not a palindrome")
elif message[::-1] == message:
    print("it is a palindrome")
else:
    print("it's not a palindrome")
