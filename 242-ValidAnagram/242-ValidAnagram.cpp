// Last updated: 4/4/2026, 12:42:02 AM
class Solution {
public:
    bool isAnagram(string s, string t) {
        int arrs[26];
        int arr[26];
        memset(arr,0,26);
        memset(arrs,0,26);
        for (int i=0;i<s.length();i++){
            arrs[(s[i]) -'a']+=1;
        }
        for (int j=0;j<t.length();j++){
            arr[(t[j])-'a']+=1;
        }
        bool fnd=true;
        if (s.length()==t.length()){
            for (int i=0;i<26;i++){
                if (arr[i]!=arrs[i]){
                    fnd=false;
                    break;
                }
            }
            
        }
        else{
            fnd=false;
        }
        return fnd;
    }
};