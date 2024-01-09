def date_monument(monuments, k):  # 1 3 5 7 8,  k = 4
    cnt_pairs = 0
    last = 0
    for first in range(len(monuments)):
        while last < len(monuments) and monuments[last] - monuments[first] <= k:
            last += 1
        cnt_pairs += len(monuments) - last  # 2 + 1
    return cnt_pairs


n, k = map(int, input().split())
monuments = list(map(int, input().split()))

print(date_monument(monuments, k))