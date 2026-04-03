// Last updated: 4/4/2026, 12:42:51 AM
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n;
    n=strs.size();
    vector <string>arr1;
    bool visit[n];
    for (int i=0;i<n;i++){
        string x;
        x=strs[i];
        arr1.push_back(x);
    }
    for (int i=0;i<arr1.size();i++){
        for (int j=0;j<arr1[i].size();j++){
        for (int k=0;k<arr1[i].size()-1;k++){
            if(arr1[i][k]>arr1[i][k+1]){
                char c=arr1[i][k];
                arr1[i][k]=arr1[i][k+1];
                arr1[i][k+1]=c;
            }
        }
    }
    }
    vector <vector<string>> ark;
    memset(visit,false,sizeof(visit));
    for(int i=0;i<n-1;i++){
        
        if(visit[i]==false){
            vector<string>arr3;
            arr3.push_back(strs[i]);
            visit[i]=true;
            for (int j=i+1;j<n;j++){
                if(arr1[i]==arr1[j] && visit[j]!=true){
                    visit[j]=true;
                    arr3.push_back(strs[j]);
                }
            }
            ark.push_back(arr3);
        }
        
    }
    if(visit[strs.size()-1]==false){
        ark.push_back({strs[strs.size()-1]});
        return ark;
    }
    return ark;
    }
};