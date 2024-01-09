# def gen_seq(l, x1, d1, a, c, m):
#     seq = [x1]
#     d = d1
#     for _ in range(l - 1):
#         seq.append(seq[-1] + d)
#         d = ((a * d + c) % m)
#     return seq
#

def left_bin_search(l, r, check, check_params):
    while l < r:
        m = (l + r) // 2
        if check(m, check_params):
            r = m
        else:
            l = m + 1
    return l


def check_is_ge(index, params):
    seq, x = params
    return seq[index] >= x


def check_is_gt(index, params):
    seq, x = params
    return seq[index] > x


def cnt_less(seq, x):
    ans = left_bin_search(0, len(seq) - 1, check_is_ge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans


def cnt_gt(seq, x):
    return len(seq) - cnt_less(seq, x + 1)


def median_merge(seq1, seq2):
    l = min(seq1[0], seq2[0])
    r = max(seq1[-1], seq2[-1])
    while l < r:
        m = (l + r) // 2
        less = cnt_less(seq1, m) + cnt_less(seq2, m)
        gt = cnt_gt(seq1, m) + cnt_gt(seq2, m)
        if less <= len(seq1) - 1 and gt <= len(seq1):
            return m
        if gt > len(seq1):
            l = m + 1
        if less > len(seq1) - 1:
            r = m - 1
    return l


n, l = map(int, input(). split())
seqs = []
for i in range(n):
    seqs.append(list(map(int,input().split())))

for i in range(n):
    for j in range(i + 1, n):
        print(median_merge(seqs[i], seqs[j]))