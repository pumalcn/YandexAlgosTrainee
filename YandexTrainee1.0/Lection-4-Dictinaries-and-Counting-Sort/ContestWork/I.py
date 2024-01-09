n = int(input())
dictLower = {}

for _ in range(n):
    s = input()
    sLower = s.lower()
    dictLower.setdefault(sLower, set()).add(s)
text = input()
mistakes = 0
for word in text.split():
    wordLower = word.lower()
    if wordLower in dictLower:
        if word not in dictLower[wordLower]:
            mistakes += 1
    elif sum(c.isupper() for c in word) != 1:
        mistakes += 1
print(mistakes)
