def solution(phone_book): 
    hash_map = {num : 0 for num in phone_book} 
    
    for nums in phone_book: 
        arr = "" 
        for num in nums: 
            arr += num
    
            # 본인일 경우 제외
            if arr in hash_map and arr != nums:       
                return False 
                
    return True