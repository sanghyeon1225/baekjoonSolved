def solution(array):
    list = [0] * (max(array)+1)
    for i in array:
        list[i] += 1
    max_num = 0
    count = 0
    index = 0
    
    if(list.count(max(list)) > 1):
        return -1
    else:
        return list.index(max(list))
