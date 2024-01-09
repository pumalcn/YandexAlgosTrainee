# a = list(map(int, input().split()))
# a = sorted(a)
# if a[0] * a[1] * a[len(a) - 1] > a[len(a) - 1] * a[len(a) - 2] * a[len(a) - 3]:
#     print(a[0], a[1], a[len(a) - 1])
# else:
#     print(a[-3], a[-2], a[-1])

def kth_rearrange(seq, k):  # Алгоритм поиска k-той порядковой статистики
    left = 0
    right = len(seq) - 1
    while left < right:
        x = seq[(right + left) // 2]
        eqxfirst = left
        gtxfirst = left
        for i in range(left, right+1):
            now = seq[i]
            if now == x:
                seq[i] = seq[gtxfirst]
                seq[gtxfirst] = now
                gtxfirst += 1
            elif now < x:
                seq[i] = seq[gtxfirst]
                seq[gtxfirst] = seq[eqxfirst]
                seq[eqxfirst] = now
                gtxfirst += 1
                eqxfirst += 1
        if k < eqxfirst:
            right = eqxfirst - 1
        elif k >= eqxfirst:
            left = gtxfirst
        else:
            return


seq = list(map(int, input().split()))

kth_rearrange(seq, len(seq) - 1)
kth_rearrange(seq, len(seq) - 2)
kth_rearrange(seq, 2)

if seq[-1] * seq[-2] * seq[-3] >= seq[-1] * seq[0] * seq[1]:
    print(seq[-1], seq[-2], seq[-3])
else:
    print(seq[-1], seq[0], seq[1])