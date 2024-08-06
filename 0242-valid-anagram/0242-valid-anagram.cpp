class Solution {
public:
    bool isAnagram(string s, string t) {
        //Check if strings are of equal length
        if(s.size() != t.size())
            return false;
        
        //Create variables used to to store values
        unordered_map<char, int> letterToOccurence;
        
        for(char chr: s){
            letterToOccurence[chr] += 1;
        }
        
        for(char chr: t){
            letterToOccurence[chr] -= 1;
            if(letterToOccurence[chr] < 0)
                return false;
        }
        
        return true;
    }
};