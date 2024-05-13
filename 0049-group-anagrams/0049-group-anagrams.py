class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        #isolate word from strs list
        for s in strs:
            count = [0] * 26
            
            #loop through the word to get chars present 
            for char in s:
                #get ascii values
                count[ord(char) - ord("a")] += 1
                
            result[tuple(count)].append(s)
            
        return result.values()
                
                