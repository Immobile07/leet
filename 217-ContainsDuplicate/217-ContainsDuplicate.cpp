// Last updated: 4/4/2026, 12:42:11 AM
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        bool fnd=false;
        int sz=nums.size()-1;
        sort(nums.begin(),nums.end());
        for (int i=0;i<sz;i++){
            if (nums[i]==nums[i+1]){
                fnd=true;
                break;
            }
        }
        return fnd;
    }
};