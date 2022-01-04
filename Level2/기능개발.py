def solution(progresses, speeds):
    answer = []

    while(len(progresses) > 0):
        count = 0

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        while(progresses[0] >= 100):
            count += 1
            del progresses[0] # dequeue
            del speeds[0] # dequeue
            if (len(progresses) == 0): # out of range
                break

        if count > 0:
            answer.append(count)

    return answer
