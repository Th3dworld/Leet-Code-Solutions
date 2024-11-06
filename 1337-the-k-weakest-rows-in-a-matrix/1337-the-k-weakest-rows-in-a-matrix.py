class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowStrength = []
        for r in range(len(mat)):
            hashMap = Counter(mat[r])
            if 1 in hashMap:
                rowStrength.append([hashMap[1], r])
            else:
                rowStrength.append([0, r])
        heapq.heapify(rowStrength)
        res = []
        while k>0:
            res.append(heapq.heappop(rowStrength)[1])
            k -= 1
        return res
            