class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //create map to hold values
        unordered_map<int, int> index_to_value;
        for(int i = 0; i < nums.size(); i++){
            //check if element exists in map
            //return vector if elements exist
            if(index_to_value.contains(target - nums[i]))
                return {i, index_to_value[target - nums[i]]};
            
            index_to_value[nums[i]] = i;
        }
        return {};
    }
};