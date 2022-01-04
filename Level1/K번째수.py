def solution(array, commands):
    answer = []
    for factor in commands:
        i = factor[0]
        j = factor[1]
        k = factor[2]
        new_arr = array[i-1:j]
        new_arr.sort()
        answer.append(new_arr[k-1])
    return answer
