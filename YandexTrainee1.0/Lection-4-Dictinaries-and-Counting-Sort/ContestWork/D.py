keyboard_stress = {}
n = int(input())
x = input().split()
for i in range(n):
    keyboard_stress[i+1] = int(x[i])

m = int(input())

press_count_lst = [int(x) for x in input().split()]
press_count_dict = {}

for press_count in press_count_lst:
    press_count_dict[press_count] = press_count_dict.get(press_count, 0) + 1

for press_count in sorted(press_count_dict.keys()):
    if press_count_dict[press_count] > keyboard_stress[press_count]:
        print('YES')
    else:
        print('NO')
