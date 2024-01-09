import sys

words = sys.stdin.read()
my_dict = {}
for word in words.split():
    my_dict[word] = my_dict.get(word, 0) + 1

max_value = max(my_dict.values())
for key in sorted(my_dict.keys()):
    if my_dict[key] == max_value:
        print(key)
        break
