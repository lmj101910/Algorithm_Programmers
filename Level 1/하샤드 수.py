def solution(x):
    answer = False
    x = str(x)
    num_for_divide = 0
    for i in range(len(x)):
        num_for_divide += int(x[i])
    if int(x) % num_for_divide == 0:
        answer = True
    return answer
