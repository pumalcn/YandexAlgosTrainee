def unique_count(seq):
    return len(set(seq))


seq = map(int, input().split())

print(unique_count(seq))
