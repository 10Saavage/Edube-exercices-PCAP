def read_int(prompt, min, max):
    while True:
        number = input(prompt)
        try:
            number = int(number)
        except ValueError:
            print("Error: wrong input")
            continue
        try:
            assert -10 <= number <= 10
            break
        except AssertionError:
            print("Error: the value is not within permitted range ({}..{})".format(min, max))
            continue

    return number


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
