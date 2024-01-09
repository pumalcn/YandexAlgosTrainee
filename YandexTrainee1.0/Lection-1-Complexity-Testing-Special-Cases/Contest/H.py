a, b, n, m = int(input()), int(input()), int(input()), int(input())
min1 = (a + 1) * (n - 1) + 1
max1 = (a + 1) * (n - 1) + 1 + 2 * a
min2 = (b + 1) * (m - 1) + 1
max2 = (b + 1) * (m - 1) + 1 + 2 * b
min_ans = max(min1, min2)
max_ans = min(max1, max2)
if max_ans < min_ans:
    print(-1)
else:
    print(min_ans, max_ans)
