class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        res = []
        def sol(index, cum, target,ans):
            if index >= len(c):
                if target == 0:
                    ans.append(cum[:])
                return
            
            if c[index] <= target:
                cum.append(c[index])
                sol(index,cum,target-c[index],ans)
                cum.pop()
            sol(index+1,cum,target,ans)
        sol(0,[],target,res)    
        return res