c0 = int(input("enter a number non-zero integer and non negative : "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        print(c0)
    else:
        c0 = 3 * c0 + 1
        print(c0)
    steps += 1
print("steps = {}".format(steps))
