// Last updated: 4/4/2026, 12:41:14 AM
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
    bool checkTree(TreeNode* root) {
        int jogg=0;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty()){
            TreeNode * node=q.front();
            q.pop();
            jogg+=node->val;
            if(node->left!=NULL){
                q.push(node->left);
            }
            if(node->right!=NULL){
                q.push(node->right);
            }
        }
        if (jogg-(root->val)==root->val){
            return true;
        }
        else{
            return false;
        }
    }
};