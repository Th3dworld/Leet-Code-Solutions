class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = collections.defaultdict(list)
        
        
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            hashMap[tuple(count)].append(string)
        return hashMap.values()