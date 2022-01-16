def solution(n, lost, reserve):
    # lost 기준으로 체육복을 선택
    lost.sort()
    reserve.sort()
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    answer = n - len(lost_set)
    for i in lost_set:
        if (i-1) in reserve_set:
            reserve_set.remove(i-1)
            answer += 1
        elif (i+1) in reserve_set:
            reserve_set.remove(i+1)
            answer += 1
            
    return answer
