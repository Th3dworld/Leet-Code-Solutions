class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = collections.defaultdict(list)
        
        for s in strs:
            res = [0] * 26
            for c in s:
                res[ord(c) - ord('a')] += 1
            Map[tuple(res)].append(s)
        return Map.values()