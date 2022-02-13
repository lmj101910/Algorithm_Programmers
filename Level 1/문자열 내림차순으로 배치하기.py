def solution(s):
    answer = ''
    str_list = list(map(str, s))
    str_upper = []
    str_lower = []
    
    for i in str_list:
        if i.upper() == i:
            str_upper.append(i)
        elif i.lower() == i:
            str_lower.append(i)
            
    str_upper.sort(reverse=True)
    str_lower.sort(reverse=True)
    
    answer += ''.join(str_lower)
    answer += ''.join(str_upper)

    return answer

#def solution(s):
#    answer = ''
#    str_list = list(map(str, s))
#    str_list.sort(reverse=True)
#    answer += ''.join(str_list)
#
#    return answer
