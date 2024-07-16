class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        //create set to store data
        set<int> hashSet;
        //iterate through array storing data in sets
        for(int num: nums){
            if(hashSet.contains(num)){
                return true;
            }
            hashSet.insert(num);
        }
        return false;
        
    }
};