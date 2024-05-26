def canJump( nums):
    n=len(nums)
    cur=0
    for i in range(n-1,-1,-1):
        if nums[i]==0:
            cur+=1
        elif nums[i]!=0 and cur>0:
            if nums[i] > cur:
                cur=0
            else:
                cur+=1
        else:
            continue
    if cur>0:
        return False    
    else:
        return True
        






nums= [0,2,0,3,1,1,4]

print(canJump(nums))
