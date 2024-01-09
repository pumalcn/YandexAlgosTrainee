a, b, c = int(input()), int(input()), int(input())
if c < 0:
    print("NO SOLUTION")
elif (a + b) == c * c and (2 * a + b) == c * c:
    print("MANY SOLUTIONS")
else:
    if a != 0 and (c * c - b) / a == (c * c - b) // a:
        print((c * c - b) // a)
    else:
        print("NO SOLUTION")