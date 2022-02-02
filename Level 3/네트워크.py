def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            need_visit = []
            need_visit.append(i)
            while need_visit:
                index = need_visit.pop(0)
                visited[index] = True
                for node in range(n):
                    if node != index and computers[index][node] == 1:
                        if visited[node] == False:
                            need_visit.append(node)
            answer += 1
    return answer
