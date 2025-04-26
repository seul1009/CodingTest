def solution(skill, skill_trees):
    count=0
    for st in skill_trees:
        sk=''
        for s in st:
            if s in skill:
                sk+=str(skill.index(s))
        if sk=='':
            count+=1 
        num=''
        for i in range(len(sk)):
            num+=str(i)
            if sk==num:
                count+=1
            
                
    return count
            
            
                
        
        