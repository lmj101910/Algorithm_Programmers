def solution(N, number):
    s = [None] + [{int(str(N)*x)} for x in range(1, 9)]
    for i in range(1, 9): # 값을 담을 인덱스
        for j in range(1, i): # 계산할 인덱스
            for num1 in s[j]: # j는 점점 증가함, 하나씩 빼옴
                for num2 in s[i-j]: # 인덱스가 점점 감소함
                    s[i].add(num1 + num2)
                    s[i].add(num1 - num2)
                    s[i].add(num1 * num2)
                    if num2 != 0: # 0으로 나눌 수 없음
                        s[i].add(num1 // num2)
        if number in s[i]: # i 즉 해당 인덱스에 대한 계산을 마친 후 number가 해당 인덱스 set에 존재하면
            return i # 해당 인덱스 반환
            break
    else: # break가 발생하지 않으면
        return -1
