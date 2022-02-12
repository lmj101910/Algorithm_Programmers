def solution(n):
    answer = sorted(str(int(n)), reverse=True)
    return int(''.join(answer))
