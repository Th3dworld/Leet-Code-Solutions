class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //Create map to store values
        unordered_map<int, int> valueToFrequency;
        multimap<int,int> frequencyToValue;
        vector<int> solution;

        for(int num: nums){
            valueToFrequency[num] += 1;
        }

        for(auto pair : valueToFrequency){
            frequencyToValue.insert({pair.second,pair.first});
        }

        //iterator to end of container
        auto iter = frequencyToValue.end();
        iter--;

        while(k > 0){
            solution.push_back(iter->second);
            iter--;
            k--;
        }

        return solution;
    }
};