n = int(input())
events = []

for i in range(n):
    now_in, now_out = map(int, input().split())

    if now_out - now_in >= 5:
        events.append((now_in, -1, i))
        events.append((now_out - 5, 1, i))
events.sort()
if len(events) == 0:
    print(0, 10, 20)

elif len(events) == 2:
    print(1, events[0][0], events[0][0] + 10)

else:
    best_ans = 0
    first_best, second_best = 0, 0
    first_ad = set()
    for i in range(len(events)):
        try_to_play_first_add = events[i]
        if try_to_play_first_add[1] == -1:
            first_ad.add(try_to_play_first_add[2])
            if len(first_ad) > best_ans:
                best_ans = len(first_ad)
                first_best = try_to_play_first_add[0]
                second_best = try_to_play_first_add[0] + 5
        second_ad_cnt = 0
        for j in range(i + 1, len(events)):
            try_to_play_scnd_add = events[j]
            if try_to_play_scnd_add[1] == -1 and try_to_play_scnd_add[2] not in first_ad:
                second_ad_cnt += 1
            if try_to_play_scnd_add[0] - 5 >= try_to_play_first_add[0] and len(first_ad) + second_ad_cnt > best_ans:
                best_ans = len(first_ad) + second_best
                first_best = try_to_play_first_add[0]
                second_best = try_to_play_scnd_add[0]
            if try_to_play_scnd_add[1] == 1 and try_to_play_scnd_add[2] not in first_ad:
                second_ad_cnt -= 1
        if try_to_play_first_add[1] == 1:
            first_ad.remove(try_to_play_first_add[2])
    print(best_ans, first_best, second_best)
