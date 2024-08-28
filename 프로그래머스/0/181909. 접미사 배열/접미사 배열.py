def solution(my_string):
    str = []
    for i in range(1, len(my_string)+1):
        str.append(my_string[-i:])
    return sorted(str)