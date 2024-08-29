def solution(babbling):
    count = 0
    pron = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        result = 0
        for j in range(len(pron)):
            if pron[j] in i:
                result += len(pron[j])
        if result == len(i):
            count += 1
    return count