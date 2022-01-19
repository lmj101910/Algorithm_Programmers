def solution(arr):
    answer = [-1]
    tmp = min(arr)
    index = arr.index(tmp)
    del arr[index]
    if len(arr) == 0:
        return answer
    else:
        return arr
