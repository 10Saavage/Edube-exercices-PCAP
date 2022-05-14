try:
    birthday = int(input("enter your birthday: "))
except ValueError:
    print("only intergers")
    exit()

digitOfLife = 0

while True:
    for digit in str(birthday):
        digitOfLife += int(digit)

    if digitOfLife <= 9:
        break
    else:
        birthday = digitOfLife
        digitOfLife = 0

print(digitOfLife)
