def solution(nums):
    answer = 0
    pick_count = len(nums) / 2
    can_pick = len(set(nums))
    
    # 종류 판별
    if can_pick > pick_count:
        answer = pick_count
    else:
        answer = can_pick
    
    return answer
