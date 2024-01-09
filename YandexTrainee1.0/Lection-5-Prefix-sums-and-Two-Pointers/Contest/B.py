def numbers_sum(cars, k):  # 1 3 5 7 8,  k = 4
    cnt_pairs = 0
    first = 0
    now_sum = 0
    for last in range(len(cars)):
        now_sum += cars[last]
        while now_sum > k:
            now_sum -= cars[first]
            first += 1
        if now_sum == k:
            cnt_pairs += 1

    return cnt_pairs


n, k = map(int, input().split())
cars = list(map(int, input().split()))
print(numbers_sum(cars, k))
