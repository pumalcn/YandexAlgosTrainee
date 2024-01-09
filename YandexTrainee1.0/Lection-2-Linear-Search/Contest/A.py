# a = map(int, input().split())
# a = list(a)
# b = a
# if b == sorted(a) and len(set(b)) == len(a):
#     print("YES")
# else:
#     print("NO")


def growth(seq):
    flag = True
    for i in range(len(seq)-1):
        if seq[i] >= seq[i+1]:
            flag = False
    return flag


seq = [int(x) for x in input().split()]

if growth(seq):
    print('YES')
else:
    print('NO')
