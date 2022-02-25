def solution(s):
    answer = ''
    str_list = s.split(" ")
    
    for i in range(len(str_list)):
        str_split_list = list(str_list[i])
        
        for j in range(len(str_split_list)):
            if j % 2 == 0:
                str_split_list[j] = str_split_list[j].upper()
            elif j % 2 == 1:
                str_split_list[j] = str_split_list[j].lower()
                
        str_list[i] = "".join(str_split_list)
    
    answer = " ".join(str_list)
    
    return answer
