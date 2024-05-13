#include <unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //create a map that holds solutions and vector to store ascii values
        map <vector<int>, vector<string>> map1;
        vector<int> count (26,0);
        vector<string> hold;
        vector<vector<string>> result;

        //iterate through strs getting individual strings
        for(string s : strs){
            fill(count.begin(), count.end(), 0);
            hold.push_back(s);
            //loop through string to get characters present
            for(char c: s){
                count[(int)c - (int)'a'] += 1;
            }
            //populate map
            if(map1.find(count) != map1.end()){
                map1[count].push_back(s);  
            }
            else{
              map1[count] =  hold; 
            }
            hold.clear();
        }

        for(auto x : map1){
            result.push_back(x.second);
        }

        return result;
    }
};