def solution(num_list):
    odd_num = []
    even_num = []
    for i in range(len(num_list)):
        if (num_list[i] % 2 == 0):
            even_num.append(str(num_list[i]))
        else:
            odd_num.append(str(num_list[i]))
              
    odd = ''.join(odd_num)
    even  = ''.join(even_num)
    return int(odd) + int(even)
