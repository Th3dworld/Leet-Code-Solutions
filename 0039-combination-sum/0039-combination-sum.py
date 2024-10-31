class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, target, cum):
            if index >= len(candidates):
                if target == 0:
                    res.append(cum[:])
                return
            
            if candidates[index] <= target:
                cum.append(candidates[index])
                backtrack(index, target - candidates[index], cum)
                cum.pop()
            backtrack(index + 1, target, cum)
        backtrack(0,target,[])
        return res