def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] < i+1:
            answer = i
            break
        if citations[i] > i+1 and i+1 == len(citations):
            answer = i+1
    return answer
