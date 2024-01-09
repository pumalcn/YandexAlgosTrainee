def turtles_liars(statements):
    previous_statements = set()
    for statement in statements:
        should_be_positive_placements = statement[0] >= 0 and statement[1] >= 0
        correct_number_of_turtles = statement[0] + statement[1] == len(statements) - 1
        # в целом, не обязательна вторая проверка
        if should_be_positive_placements and correct_number_of_turtles and statement not in previous_statements:
            previous_statements.add(statement)

    return len(previous_statements)


assert turtles_liars([(1, 0), (1, 0)]) == 1
assert turtles_liars([(2, 0), (0, 2), (2, 2)]) == 2
assert turtles_liars([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]) == 5
assert turtles_liars([(9, 1), (8, 1), (7, 2), (6, 2), (5, 3), (4, 4), (3, 6), (2, 7), (1, 9), (8, 0)]) == 4


n = int(input())
statements = [tuple(map(int, input().split())) for _ in range(n)]
print(turtles_liars(statements))
#
# n = int(input())
#
# used_before = set()
# for i in range(n):
#     a, b = map(int, input().split())
#     if a >= 0 and b >= 0 and a + b == n - 1 and a not in used_before:
#         used_before.add(a)
#
# print(len(used_before))
