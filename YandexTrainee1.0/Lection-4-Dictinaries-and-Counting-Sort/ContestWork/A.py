def find_synonym(synonyms, word):
    synonyms_dict = {}
    for syn1, syn2 in synonyms:
        synonyms_dict[syn1], synonyms_dict[syn2] = syn2, syn1
    return synonyms_dict[word]


synonyms = [tuple(input().split()) for _ in range(int(input()))]
word = input()
print(find_synonym(synonyms, word))

