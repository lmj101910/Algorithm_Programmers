def solution(board, moves):
    answer = 0
    bucket = []
    
    for locate in moves:
        for i in range(len(board)):
            if board[i][locate-1] != 0:
                bucket.append(board[i][locate-1])
                board[i][locate-1] = 0
            
                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        del bucket[-1]
                        del bucket[-1]
                        answer += 2
                break
    return answer
