class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        # newList = c
        # newList.sort()
        c.sort()
        print(c)
        res = []
        def com(index,target,cumm):
            if target == 0:
                res.append(cumm[:])
                print(res)
                return
            
            for i in range(index, len(c)):
                if i > index and c[i] == c[i-1]: 
                    continue
                if c[i] > target: 
                    break
                cumm.append(c[i])
                com(i+1, target-c[i], cumm)
                cumm.pop()
            
        com(0,target,[])
        return res
            
#     c.sort()  # Sort the list to handle duplicates
#     res = []  # Result list to store combinations

#     def com(index, target, cumm):
#         if target == 0:  # Base case: if target is met
#             res.append(cumm[:])  # Add the current combination to the result
#             return
        
#         for i in range(index, len(c)):
#             if i > index and c[i] == c[i - 1]:  # Skip duplicates
#                 continue
#             if c[i] > target:  # Stop if current element exceeds target
#                 break
#             cumm.append(c[i])  # Include current element in the combination
#             com(i + 1, target - c[i], cumm)  # Move to the next element
#             cumm.pop()  # Backtrack by removing the last element

#     com(0, target, [])
#     return res
            