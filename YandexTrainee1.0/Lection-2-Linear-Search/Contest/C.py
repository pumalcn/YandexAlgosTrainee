n = int(input())
seq = list(map(int, input().split()))
b = int(input())

min_dif = abs(b - seq[0])
ans = 0
pos = 0
for i in range(len(seq)):
    if abs(b - seq[i]) <= min_dif:
        min_dif = abs(b - seq[i])
        ans = seq[i]
print(ans)
