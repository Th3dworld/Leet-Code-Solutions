class Solution:
    def largestInteger(self, num: int) -> int:
        string = str(num)
        string = list(string)
        parity = []
        
        for s in string:
            if int(s)%2 == 0:
                parity.append(0)
            else:
                parity.append(1)
        
        for i in range(len(string)):
            for j in range(i+1, len(string)):
                if string[i] < string[j] and parity[i] == parity[j]:
                    string[i],string[j] = string[j],string[i]
        
        return int("".join(string))
        