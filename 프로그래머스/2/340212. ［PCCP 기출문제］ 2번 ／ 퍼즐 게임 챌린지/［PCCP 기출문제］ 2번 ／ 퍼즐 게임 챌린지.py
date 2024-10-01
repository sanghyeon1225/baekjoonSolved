def solution(diffs, times, limit):
    max_level, min_level = max(diffs), 1
    while(min_level < max_level):
        mid = (min_level + max_level) // 2
        
        trys = 0
        answer = 0
        
        for i in range(len(diffs)):
            if (diffs[i] <= mid):
                answer += times[i]
            else:
                trys = diffs[i] - mid
                if (i == 0):
                    answer += (trys + 1) * (times[i])
                else:
                    answer += trys * (times[i-1] + times[i]) + times[i]
        if (answer > limit):
            min_level = mid + 1
        else:
            max_level = mid
    return min_level