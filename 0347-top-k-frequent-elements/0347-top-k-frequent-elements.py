class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create variables
        count = dict()
        results = list()

        #iterate through the array store element as key
        #and number of occurence as value
        for num in nums:
            if num in count.keys():
                count[num] += 1
            else:
                count[num] = 1

        #Get list containing values
        values = list(count.values())
        values.sort()
        values = values[-k:]

        for key, value in count.items():
            if value in values:
              results.append(key)

        return results