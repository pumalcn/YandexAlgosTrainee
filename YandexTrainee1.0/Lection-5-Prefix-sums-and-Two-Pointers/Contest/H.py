import math
from collections import defaultdict


def substring(input_str, k):  # ababa 2
    best_result = (-math.inf, 0)
    left = 0
    counter = defaultdict(int)
    substring_len = 0
    for right_char in input_str:
        while counter[right_char] >= k:
            counter[input_str[left]] -= 1  # {'a': 1}
            substring_len -= 1  # 3
            left += 1

        counter[right_char] += 1  # {'a': 2, 'b': 2}
        substring_len += 1
        if substring_len > best_result[0]:
            best_result = (substring_len, left + 1)  # (1, 1), (2, 1), (3, 1), (4, 1), (4, 2)

    return best_result


n, k = map(int, input().split())

input_str = input()

print(*substring(input_str, k))
