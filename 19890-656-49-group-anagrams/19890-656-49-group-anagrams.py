class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        
        for string in strs:
            mapKey = [0] * 26
            
            for char in string:
                mapKey[ord(char) - ord('a')] += 1
            
            res[tuple(mapKey)].append(string)
        
        return list(res.values())
    