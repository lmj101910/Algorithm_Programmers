def solution(s):
    answer = True
    count_p = 0
    count_y = 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            count_p += 1
        elif s[i] == 'y' or s[i] == 'Y':
            count_y += 1
    if count_y != count_p:
        answer = False

    return answer
