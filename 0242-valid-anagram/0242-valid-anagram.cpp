class Solution {
public:
    bool isAnagram(string s, string t) {
        //Check if strings are of equal length 
        if(s.length() != t.length()){
            return false;
        }
        
        //create map to store letter to number of times it occurs
        unordered_map<char, int> letterOccurence;
        
        for(char c: s){
            letterOccurence[c] += 1;
        }
        
        for(char c: t){
            letterOccurence[c] -= 1;
            if(letterOccurence[c] < 0){
                return false;
            }
        }
        
        return true;
    }
};