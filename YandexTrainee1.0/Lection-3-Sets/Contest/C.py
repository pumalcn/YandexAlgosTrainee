def cubes(colors_a, colors_b):
    set_a = set(colors_a)
    set_b = set(colors_b)
    return list(map(sorted, [set_a & set_b, set_a - set_b, set_b - set_a]))


assert cubes([0, 1, 10, 9], [1, 3, 0]) == [[0, 1], [9, 10], [3]]
assert cubes([1, 2], [2, 3]) == [[2], [1], [3]]
assert cubes([], []) == [[], [], []]


n, m = map(int, input().split())
first_colors = [int(input()) for _ in range(n)]
second_colors = [int(input()) for _ in range(m)]
results = cubes(first_colors, second_colors)
for result in results:
    print(len(result))
    print(*result)





