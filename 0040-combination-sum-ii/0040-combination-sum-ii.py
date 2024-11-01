class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        c.sort()
        res = []
        def back(index, target, ds):
            if target == 0:
                res.append(ds[:])
                return
            
            for i in range(index, len(c)):
                if i > index and c[i] == c[i-1]: 
                    continue
                if c[i] > target:
                    break
                ds.append(c[i])
                back(i+1, target - c[i], ds)
                ds.pop()
        back(0,target,[])
        return res
                    