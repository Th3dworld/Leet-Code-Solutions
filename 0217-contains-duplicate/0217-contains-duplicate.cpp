class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int,int> valuesPresent {};

        //If value is present return true
        for(int x: nums)
        {
            if(valuesPresent.contains(x))
            {
                return true;
            }
            else
                valuesPresent[x] = 1;
        }
        return false;        
    }
};