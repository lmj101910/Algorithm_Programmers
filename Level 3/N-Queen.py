def is_availabe(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        # 수직 체크와 대각선 체크
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def DFS(n, current_row, current_candidate, result):
    if current_row == n:
        result.append(current_candidate[:])
        return

    for candidate_col in range(n):
        if is_availabe(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(n, current_row + 1, current_candidate, result)
            current_candidate.pop()

def solution(n):
    answer = 0
    result = []
    DFS(n, 0, [], result)
    return len(result)
