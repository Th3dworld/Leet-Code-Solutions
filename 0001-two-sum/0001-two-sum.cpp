class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //Create map to map value to index
        unordered_map<int,int>valueToIndex;
        
        //iterate through vector adding values and index to map
        //and checking if values that add to target exist
        for(int i = 0; i < nums.size(); i++){
            if(valueToIndex.contains(target - nums[i])){
                return {i, valueToIndex[target - nums[i]]};
            }
            valueToIndex[nums[i]] = i;
        }
        return {};
    } 
};