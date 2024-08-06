class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //Create variable that will map values to index
        unordered_map<int,int> valueToIndex;
        
        //iterate through vector populating map and checking if value that adds up to target exists
        for(int i = 0; i < nums.size(); i++){
            if(valueToIndex.contains(target - nums[i])){
                return {i, valueToIndex[target - nums[i]]};
            }
            valueToIndex[nums[i]] = i;
        }
        
        return {};
    }
};