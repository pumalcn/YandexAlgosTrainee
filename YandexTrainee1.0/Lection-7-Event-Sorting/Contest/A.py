def count_not_cheaters(f_num_of_students, f_vision_of_teacher):
    events = []

    for vision in f_vision_of_teacher:
        vision_start, vision_end = vision
        events.append((vision_start, -1))
        events.append((vision_end, 1))
    events.sort()

    unobserved_student_count = f_num_of_students
    segment_start = None
    cnt_of_covered_students = 0
    for event in events:
        if event[1] == -1:
            if cnt_of_covered_students == 0:
                segment_start = event[0]
            cnt_of_covered_students += 1
        else:
            cnt_of_covered_students -= 1
            if cnt_of_covered_students == 0:
                unobserved_student_count -= (event[0] - segment_start + 1)
    return unobserved_student_count


num_of_students, num_of_teachers = map(int, input().split())
vision_of_teacher = [map(int, input().split()) for _ in range(num_of_teachers)]
print(count_not_cheaters(num_of_students, vision_of_teacher))
