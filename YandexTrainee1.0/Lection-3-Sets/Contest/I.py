# n = int(input())
# set_ans = set()
# for _ in range(n):
#     set_lang = [input() for _ in range(int(input()))]
#     for lang in set_lang:
#         if lang not in set_ans:
#             set_ans.add(lang)
#
# print(*set_ans)


def polyglots(students):
    return [
        students[0].intersection(*students[1:]),
        students[0].union(*students[1:])
    ]


n = int(input())
students = []
for _ in range(n):
    m = int(input())
    students.append({input() for _ in range(m)})
results = polyglots(students)
for result in results:
    print(len(result))
    for language in result:
        print(language)
