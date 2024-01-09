k = int(input())
ans = [''] * k
for test in range(k):
    nums = list(map(int, input().split()))
    n = nums[0]
    events = [0] * (2 * n)
    for i in range(1, len(nums), 2):
        events[i - 1] = (nums[i], -1, i)
        events[i] = (nums[i + 1], 1, i)

    events.sort()
    good_seq = set()
    now_seq = set()
    good_flag = True
    prev_time = -1
    for event in events:
        if event[0] != 0 and len(now_seq) == 0:
            good_flag = False
            break
        if len(now_seq) == 1 and event[0] != prev_time:
            good_seq.update(now_seq)
        if event[1] == -1:
            now_seq.add(event[2])
        else:
            now_seq.remove(event[2])
        prev_time = event[0]
    if events[-1][0] != 10_000:
        good_flag = False
    if good_flag and len(good_seq) == n:
        ans[test] = 'Accepted'
    else:
        ans[test] = 'Wrong Answer'
print('\n'.join(ans))