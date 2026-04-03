// Last updated: 4/4/2026, 12:41:44 AM
class Solution {
  
public:
static bool cmp(pair<int,int>a,pair<int,int>b ){
    return b.second< a.second;
}
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<pair<int,int>>arr;
      
    vector<int>arr2;
    int n;
    n=nums.size();
    bool visit[n];
memset(visit,false,sizeof(visit));
    for (int i=0;i<n-1;i++){
        int cnt=1;
        if(visit[i]==false){
            visit[i]=true;

        for (int j=i+1;j<n;j++){
            if (nums[i]==nums[j]){
                cnt++;
                visit[j]=true;
            }
        }
        arr.push_back({nums[i],cnt});
    }
    }
    
    vector <int>fnl;
    if(visit[nums.size()-1]==false){
        arr.push_back({nums[nums.size()-1],1});
        sort(arr.begin(),arr.end(),cmp);
        for (int i=0;i<k;i++){
            fnl.push_back(arr[i].first);
        }
        return fnl;
    }
    else{
        sort(arr.begin(),arr.end(),cmp);
        for (int i=0;i<k;i++){fnl.push_back(arr[i].first);
        }
        return fnl;
    }
    
    }
};