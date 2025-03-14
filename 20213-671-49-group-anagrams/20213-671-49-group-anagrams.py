class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = collections.defaultdict(list)
        
        for s in strs:
            counter = [0] * 26
            
            for ch in s:
                counter[ord(ch)-ord('a')] += 1
            
            hashMap[tuple(counter)].append(s)
        
        return list(hashMap.values())
                
                
        
        