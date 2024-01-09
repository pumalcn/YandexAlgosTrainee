n, k = map(int, input().split())
x = list(map(int, input().split()))

cnt_nums = {}

for now in x:
    if now not in cnt_nums:
        cnt_nums[now] = 0
    cnt_nums[now] += 1  # {1: 2, 2: 2, 3: 1}

uniq_nums = list(cnt_nums.keys())  # [1, 2, 3]
uniq_nums.sort()

r = 0
ans = 0
duplicates = 0

for l in range(len(uniq_nums)):  # 0 1
    while r < len(uniq_nums) and uniq_nums[l] * k >= uniq_nums[r]:
        if cnt_nums[uniq_nums[r]] >= 2:
            duplicates += 1  # 2
        r += 1  # 1, 2, 3

    range_len = r - l  # 2 - 0, 3 - 1
    if cnt_nums[uniq_nums[l]] >= 2:
        ans += (range_len - 1) * 3  # 0 + 2 - 1 * 3, 6 + (2 - 1) * 3
    if cnt_nums[uniq_nums[l]] >= 3:
        ans += 1
    ans += (range_len - 1) * (range_len - 2) * 3  # (2 - 1) * 0 * 3, + 0
    if cnt_nums[uniq_nums[l]] >= 2:
        duplicates -= 1  # 1 0
    ans += duplicates * 3  # 3 + 1 * 3, 9 + 0
print(ans)