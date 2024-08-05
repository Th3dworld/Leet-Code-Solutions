class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //Create variables
        map<vector<int>, vector<string>> mapr;
        vector <int> holdr(26,0);
        vector<vector<string>> res;
        
        for(string str: strs){
            fill(holdr.begin(), holdr.end(), 0);
            for(char chr: str){
                holdr[(int)chr - (int)'a'] += 1;
            }
            mapr[holdr].push_back(str);
        }
        
        for(auto pair: mapr)
            res.push_back(pair.second);
        return res;
    }
};


