// Last updated: 4/4/2026, 12:41:27 AM
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        bool flagger=true;
        queue <TreeNode*> q;
        q.push(root);
        while (!q.empty()){
            TreeNode* node=q.front();
            q.pop();

            if(node->val==root->val){
                if (node->left!=NULL){
                    q.push(node->left);
                }
                if(node->right!=NULL){
                    q.push(node->right);
                }
                continue;

            }
            else{
                flagger=false;
                break;
            }
            

        }
        return flagger;
    }
};
        