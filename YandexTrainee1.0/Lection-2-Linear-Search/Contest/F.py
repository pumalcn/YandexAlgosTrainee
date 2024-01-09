def make_symmetric(sequence):
    for i in range(len(sequence)):
        if sequence[i:] == sequence[i:][::-1]:
            additional_numbers = sequence[:i][::-1]
            return len(additional_numbers), additional_numbers


n = int(input())
seq = list(map(int, input().split()))
count, numbers = make_symmetric(seq)
print(count)
if count > 0:
    print(*numbers)
