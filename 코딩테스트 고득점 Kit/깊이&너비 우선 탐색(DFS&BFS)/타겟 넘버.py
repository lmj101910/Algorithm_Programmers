from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-numbers[0],0])
    while queue:
        temp, index = queue.popleft()
        index += 1
        if index < n:
            queue.append([temp+numbers[index], index])
            queue.append([temp-numbers[index], index])
        else:
            if temp == target:
                answer += 1   
    return answer
