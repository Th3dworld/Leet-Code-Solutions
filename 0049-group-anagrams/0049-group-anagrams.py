class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        
        for string in strs:
            key = ""
            for char in sorted(string):
                key += str(ord(char))
            hashMap[key].append(string)
        
        return hashMap.values()
        