// Last updated: 4/4/2026, 12:41:36 AM
#include <vector>
#include <utility>

class Solution {
public:
int smcl;
    int n;
    int m;
    std::vector<std::pair<int, int>> cmn = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
    std::vector<std::vector<int>> filled;
    bool vis[1005][1005];

    bool validator(int ek, int dui, std::vector<std::vector<int>>& image) {
        if (ek < 0 || dui < 0 || ek >= n || dui >= m || image[ek][dui] < 0) {
            return false;
        } else {
            return true;
        }
    }

    void dfs(std::vector<std::vector<int>>& image, int sr, int sc, int color) {
        vis[sr][sc] = true;
        image[sr][sc]=color;
        for (int i = 0; i < 4; i++) {
            int ek = sr + cmn[i].first;
            int dui = sc + cmn[i].second;
            if (validator(ek, dui, image) && !vis[ek][dui] && image[ek][dui] == smcl) {
                image[ek][dui] = color;
                dfs(image, ek, dui, color);
            }
        }
    }

    std::vector<std::vector<int>> floodFill(std::vector<std::vector<int>>& image, int sr, int sc, int color) {
        n = image.size();
        m = image[0].size();
        if (image[sr][sc] == color) {
            return image;
        } 
        
        else {
            smcl=image[sr][sc];
            dfs(image, sr, sc, color);
            return image;
        }
    }
};
