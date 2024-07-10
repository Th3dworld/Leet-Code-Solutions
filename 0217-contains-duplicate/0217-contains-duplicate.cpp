class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int>trackr;
        for(int i: nums){
            if(trackr.contains(i))
                return true;
            trackr.insert(i);
        }
        return false;
    }
};