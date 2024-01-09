def chunked(st, n):
    st = st.split()
    a = [[] for _ in range(0, len(st), n)]
    for i in range(len(a)):
        a[i].extend(st[:n])
        st = st[n:]
    return a


string = input()
num = int(input())
string = string.split()
print(chunked(string, num))