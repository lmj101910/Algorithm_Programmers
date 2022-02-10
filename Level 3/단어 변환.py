begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

def check(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
        if count > 1:
            return False
    return True
        
def solution(begin, target, words):
    answer = 1
    if target not in words:
        answer = 0
    else:
        target_list = []
        target_list.append(begin)
        while True:
            n = len(target_list)
            for i in range(n):
                word = target_list.pop(0)
                for j in words:
                    if check(word, j) == True:
                        target_list.append(j)
            if target in target_list:
                break
            else:
                answer += 1     
    return answer
