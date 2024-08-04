class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create dictionary to store words as list
        res = collections.defaultdict(list)
        
        #create array to store occurrence of letters
        for string in strs:
            count = [0] * 26            
            for char in string:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(string)
        return res.values()
        