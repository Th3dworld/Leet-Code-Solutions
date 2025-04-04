class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list) 
        
        for s in strs:
            key = [0] * 26

            for ch in s:
                key[ord(ch) - ord('a')] += 1
            
            groups[tuple(key)].append(s)
        
        return groups.values()