class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>>mapr;
        vector <int> count(26,0);
        vector<vector<string>> res;
        
        for(string str: strs){
            fill(count.begin(), count.end(), 0);
            for(char chr: str){
                count[(int)chr - int('a')] += 1;
            }
            mapr[count].push_back(str);
        }
        
        for(auto pair: mapr){
            res.push_back(pair.second);
        }
        
        return res;
    }
};