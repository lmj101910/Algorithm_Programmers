def solution(answers):
    answer = []
    score = [0,0,0]
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    # 1번 수포자
    index1 = 0
    for i in range(len(answers)):
        if student1[index1] == answers[i]:
            score[0] += 1
        if index1 == 4:
            index1 = 0
        else: index1 += 1
    # 2번 수포자
    index2 = 0
    for i in range(len(answers)):
        if student2[index2] == answers[i]:
            score[1] += 1
        if index2 == 7:
            index2 = 0
        else: index2 += 1
    # 3번 수포자
    index3 = 0
    for i in range(len(answers)):
        if student3[index3] == answers[i]:
            score[2] += 1
        if index3 == 9:
            index3 = 0
        else: index3 += 1
    # 결과 계산
    max_score = max(score)
    for i in range(3):
        if score[i] == max_score:
            answer.append(i+1)
    return answer
