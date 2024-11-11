class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = collections.defaultdict(list)
        
        for i in strs:
            chars = [0] * 26
            for ch in i:
                chars[ord(ch) - ord('a')] += 1
            Map[tuple(chars)].append(i)
        
        return list(Map.values())