// Last updated: 4/4/2026, 12:43:00 AM
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> indices;
        bool found=false;
        int sz=nums.size();
        for(int i=0;i<sz-1;i++){
            for (int j=i+1;j<sz;j++){
                if((nums[i]+nums[j]) ==target){
                    indices.push_back(i);
                    indices.push_back(j);
                    found=true;
                    break;
                }
            
            }

            if (found==true) break;

        }
        return indices;
    }
};