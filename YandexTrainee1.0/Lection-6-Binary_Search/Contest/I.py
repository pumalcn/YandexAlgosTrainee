def check(m, check_params):
    min_brigades, c, heights = check_params  # 2, 3, [130, 160, 170, 190, 205, 225, 225, 260]
    i = 0
    brigades = 0
    while i < len(heights) - c + 1:  # 8 - 3 + 1 = 6
        if heights[i + c - 1] - heights[i] == m:  # 170 - 130 == 65
            brigades += 1
            i += c

        else:
            i += 1
    return brigades >= min_brigades


def left_binary_search(l, r, check, check_params):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, check_params):
            l = m
        else:
            r = m - 1
    return r

n, r, c = map(int, input().split())
heights = []

for _ in range(n):
    heights.append(int(input()))
heights.sort()
print(left_binary_search(0, heights[-1] - heights[0], check, (r, c, heights)))