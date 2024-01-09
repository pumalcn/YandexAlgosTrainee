temps = input().split()
t_room, t_cond = temps[0], temps[1]

mode = input()


if mode == 'freeze':
    if t_room > t_cond:
        print(t_cond)
    else:
        print(t_room)

elif mode == 'heat':
    if t_room < t_cond:
        print(t_cond)
    else:
        print(t_room)

elif mode == 'auto':
    print(t_cond)

elif mode == 'fan':
    print(t_room)
