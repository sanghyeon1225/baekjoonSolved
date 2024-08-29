def solution(s):
    num_list = s.split(" ")
    min = int(num_list[0])
    max = int(num_list[0])
    
    for i in range(1,len(num_list)):
        num = int(num_list[i])
        if(num > max):
            max = num
        if(num < min):
            min = num
    return f"{min} {max}"