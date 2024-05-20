class Solution:
    def solve(self,n):
        mid=0
        ed=10
        st=1
        while (st<=ed):
            mid = st + (ed - st) // 2
            x= (mid +(mid**2))//2
            
            if x <= n:
                st=mid+1

            else:
                ed=mid-1

        return ed
    
    
    def arrangeCoins(self, n: int) -> int:
        
        return self.solve(n)
    


n = 4
x=Solution()

print(x.arrangeCoins(n))