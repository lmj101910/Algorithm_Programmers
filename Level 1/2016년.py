def solution(a, b):
    answer = ''
    sum = 0
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in range(a - 1):
        sum += days[month]
    sum += b
    answer = day[sum % 7]
    return answer
