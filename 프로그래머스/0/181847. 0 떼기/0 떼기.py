def solution(n_str):
    for i in range(len(n_str)):
        if(int(n_str[i]) != 0):
            return n_str[i:]
    return n_str