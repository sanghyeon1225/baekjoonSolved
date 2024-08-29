def solution(num_list):
    o = 0
    e = 0
    for i in range(0, len(num_list),2):
        o += num_list[i]
    for i in range(1, len(num_list),2):
        e += num_list[i]
    if e > o:
        return e
    else:
        return o