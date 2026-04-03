// Last updated: 4/4/2026, 12:41:56 AM
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n;
    n=nums.size();
    vector <int> mlt;
    int lft=1;
    for (int i=0;i<n;i++){
        mlt.push_back(lft);
        lft*=nums[i];
        
    }
    int right=1;
    for (int i=n-1;i>=0;i--){
        mlt[i]*=right;
        right*=nums[i];
    }
    return mlt;
    }
};