def point_inclusions_count(segments, points):
    events = []
    SEGMENT_START = -1
    SEGMENT_END = 1
    POINT = 0
    for segment in segments:
        segment.sort()
        events.append((segment[0], SEGMENT_START))
        events.append((segment[1], SEGMENT_END))
    for i, point in enumerate(points):
        events.append((point, POINT, i))
    events.sort()

    results = [None] * len(points)
    current_segments_count = 0
    for event in events:
        event_type = event[1]
        if event_type == SEGMENT_START:
            current_segments_count += 1
        elif event_type == SEGMENT_END:
            current_segments_count -= 1
        elif event_type == POINT:
            idx = event[2]
            results[idx] = current_segments_count

    return results




n, m = map(int, input().split())
segments = [list(map(int, input().split())) for _ in range(n)]
points = list(map(int, input().split()))
print(*point_inclusions_count(segments, points))

