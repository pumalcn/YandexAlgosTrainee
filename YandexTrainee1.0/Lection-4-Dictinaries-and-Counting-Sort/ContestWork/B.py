import sys

words = sys.stdin.read()
my_dict = {}
for word in words.split():
    if word not in my_dict:
        my_dict[word] = 0
    print(my_dict[word], end=' ')
    my_dict[word] += 1


