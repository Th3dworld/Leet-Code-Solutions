class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = collections.defaultdict(list)
        
        for string in strs:
            key = [0] * 26 
            
            for char in string:
                key[ord(char) - ord('a')] += 1
                
            group[tuple(key)].append(string)
        
        return list(group.values())
        