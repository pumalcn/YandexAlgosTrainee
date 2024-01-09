def make_minutes(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)


n, m = map(int, input().split())
cnt_buses = [0] * (n + 1)
bus_balance = [0] * (n + 1)
events = []
over_midnight = 0

for i in range(m):
    city_dep, dep_time, city_arr, arr_time = input().split()
    city_dep = int(city_dep)
    city_arr = int(city_arr)
    dep_time = make_minutes(dep_time)
    arr_time = make_minutes(arr_time)
    if arr_time < dep_time:
        over_midnight += 1
    bus_balance[city_dep] -= 1
    bus_balance[city_arr] += 1
    events.append((dep_time, 1, city_dep))
    events.append((arr_time, -1, city_arr))
dis_balance = False
for i in range(n + 1):
    if bus_balance[i] != 0:
        dis_balance = True
if dis_balance:
    print(-1)
else:
    events.sort()
    for event in events:
        if event[1] == -1:
            cnt_buses[event[2]] += 1
        else:
            if cnt_buses[event[2]] > 0:
                cnt_buses[event[2]] -= 1
    ans = 0
    for i in range(n + 1):
        ans += cnt_buses[i]
    print(ans + over_midnight)

# 2 20:00 1 10:00 events = [(20:00, 1, 2), (10:00, -1, 1)]
