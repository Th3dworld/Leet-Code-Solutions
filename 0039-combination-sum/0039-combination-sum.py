class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        self.res = []
        def backtrack(index,cum,target,arr):
            if index == len(arr):
                if target == 0:
                    print(cum)
                    self.res.append(cum[:])
                return
            
            if arr[index] <= target:
                cum.append(arr[index])
                backtrack(index,cum,target - arr[index],arr)
                cum.pop()
                
            backtrack(index+1,cum,target,arr)
        
        backtrack(0,[],target,c)
        return self.res
            