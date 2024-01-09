def clean_phone(phone):
    clear_phone = ""
    for i in phone:
        if i not in "+-()":
            clear_phone += i
    if len(clear_phone) == 11:
        clear_phone = clear_phone[1:]
    if len(clear_phone) == 7:
        clear_phone = '495' + clear_phone
    return clear_phone


phone_to_add = input()
phone_to_add = clean_phone(phone_to_add)
for _ in range(3):
    existed_phone = input()
    existed_phone = clean_phone(existed_phone)
    if phone_to_add == existed_phone:
        print("YES")
    else:
        print("NO")
