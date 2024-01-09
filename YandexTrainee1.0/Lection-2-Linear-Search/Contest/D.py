def cnt_bigger(sequence):
    return sum(1 for i in range(1, len(sequence) - 1) if sequence[i] > sequence[i-1] and sequence[i] > sequence[i+1])


seq = [int(x) for x in input().split()]
print(cnt_bigger(seq))
