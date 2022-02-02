from collections import deque

def bfs(start, visited, graph):
    count = 0
    need_visit = [[start, count]]
    
    # 1번부터 차례로 방문하며 count를 넣어준다 이 때, count는 계속 1씩 증가한다.
    while need_visit:
        node = need_visit.pop(0)
        start = node[0]
        count = node[1]
        
        if visited[start] == -1: # 방문을 안했으면
            visited[start] = count
            count += 1
            for e in graph[start]: # 해당 노드의 인접 노드를 방문할 노드 리스트에 넣어준다
                need_visit.append([e,count])
            
            
def solution(n, edge):
    answer = 0
    graph = [[] for i in range(n+1)]
    visited = [-1 for i in range(n+1)]
    
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    bfs(1,visited,graph)
    
    answer = visited.count(max(visited))
    return answer
