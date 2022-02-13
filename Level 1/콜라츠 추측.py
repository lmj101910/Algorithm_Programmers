def solution(num):
    answer = -1
    
    if num == 1:
        return 0
    else:
        for i in range(500):
            if num % 2 == 0:
                num = num / 2
            elif num % 2 != 0:
                num = num * 3 + 1
            if num == 1:
                return i + 1
                
    return answer
