class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        //Create set to add values to 
        unordered_set<int>hash_set;

        //iterate through array adding values to dict
        for(int num: nums){
            if(hash_set.contains(num)){
                //return true if number found in set
                return true;
            }
            //insert number to set
            hash_set.insert(num);
        }
        //if duplicate not found return false
        return false;
    }
};