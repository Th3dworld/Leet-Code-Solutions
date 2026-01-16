class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arrs = collections.defaultdict(list)

        for s in strs:
            countr = [0] * 26
            for c in s:
                countr[ord(c) - ord('a')] += 1
            arrs[tuple(countr)].append(s)
        
        return list(arrs.values())