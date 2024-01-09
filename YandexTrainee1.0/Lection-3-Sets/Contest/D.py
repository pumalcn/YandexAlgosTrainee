import sys

# words = [word.lower().strip('.,;:-?!') for word in input().split()]
#
# print(len(set(words)))


def count_unique_words(text):
    return len(set(text.split()))


assert count_unique_words('''She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.''') == 19

print(count_unique_words(sys.stdin.read()))
