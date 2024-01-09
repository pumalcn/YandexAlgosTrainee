def stylish_look(t_shirts, pants):
    i = j = 0
    best_i = 0
    best_j = 0
    best_result = float('inf')
    while i < len(t_shirts) and j < len(pants):
        if t_shirts[i] == pants[j]:
            return t_shirts[i], pants[j]
        new_result = abs(pants[j] - t_shirts[i])
        if new_result < best_result:
            best_i, best_j, best_result = i, j, new_result
        if t_shirts[i] > pants[j]:
            j += 1
        else:
            i += 1
    return t_shirts[best_i], pants[best_j]


n = int(input())
t_shirts = list(map(int, input().split()))
m = int(input())
pants = list(map(int, input().split()))
print(*(stylish_look(t_shirts, pants)))
