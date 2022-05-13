message = input("enter a text: ").lower()
message = message.replace(' ', '')
if message[::-1] == message:
    print("it's a palindrome")
else:
    print("it's not a palindrome")
    
