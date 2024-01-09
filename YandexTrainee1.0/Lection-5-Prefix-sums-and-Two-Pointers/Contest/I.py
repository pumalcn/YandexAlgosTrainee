k = int(input())
s = input()

prev_len = 0
ans = 0
for i in range(k, len(s)):
    if s[i] == s[i -k]:
        prev_len += 1
        ans += prev_len
    else:
        prev_len = 0

print(ans)