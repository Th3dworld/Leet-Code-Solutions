class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lettersToGroup = collections.defaultdict(list)

        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord('a')] += 1
            lettersToGroup[tuple(key)].append(string)

        return list(lettersToGroup.values())