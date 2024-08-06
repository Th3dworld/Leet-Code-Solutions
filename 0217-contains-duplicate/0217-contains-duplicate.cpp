class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        //create set to store values
        set <int> checkForDups;
        
        //iterate through vector checking 
        for(int num: nums){
            if(checkForDups.contains(num)){
                return true;
            }
            checkForDups.insert(num);
        }       
        return false;
    }
};