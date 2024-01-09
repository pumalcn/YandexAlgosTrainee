# n, m, k = map(int, input().split())
# mines = [tuple(map(int, input().split())) for _ in range(k)]
# field = []
#
# for x in range(n):
#     field.append([])
#     for y in range(m):
#         if (x + 1, y + 1) not in mines:
#             field[x].append(
#                 sum((i, j) in mines
#                     for i in range(x, x + 3)
#                     for j in range(y, y + 3)))
#         else:
#             field[x].append("*")
#
# for row in field:
#     print(*row)


def make_field(n, m, mines):
    dx = (-1, -1, -1,  0, 0,  1, 1, 1)
    dy = (-1,  0,  1, -1, 1, -1, 0, 1)
    field = []
    for k in range(n + 2):
        field.append([0] * (m + 2))

    for minei, minej in mines:
        for k in range(len(dx)):
            field[minei + dx[k]][minej + dy[k]] += 1
    for minei, minej in mines:
        field[minei][minej] = '*'
    return field


n, m, k = map(int, input().split())

mines = []

for i in range(k):
    mines.append(tuple(map(int, input().split())))
field = make_field(n, m, mines)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(field[i][j], end=' ')
    print()
