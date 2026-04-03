// Last updated: 4/4/2026, 12:41:38 AM
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
    int eachnodesum(TreeNode* root) {
        queue<TreeNode*> baam;
        queue<TreeNode*> daan;
        int baamsm = 0;
        int daansm = 0;

        if (root->left != NULL) {
            baam.push(root->left);
            while (!baam.empty()) {
                TreeNode* l = baam.front();
                baam.pop();
                baamsm += l->val;
                if (l->left != NULL) {
                    baam.push(l->left);
                }
                if (l->right != NULL) {
                    baam.push(l->right);
                }
            }
        }

        if (root->right != NULL) {
            daan.push(root->right);
            while (!daan.empty()) {
                TreeNode* r = daan.front();
                daan.pop();
                daansm += r->val;
                if (r->left != NULL) {
                    daan.push(r->left);
                }
                if (r->right != NULL) {
                    daan.push(r->right);
                }
            }
        }

        return abs(baamsm - daansm);
    }

    int findTilt(TreeNode* root) {
        if (root == NULL || (root->left == NULL && root->right == NULL)) {
            return 0;
        }

        int x = 0;
        queue<TreeNode*> f;
        f.push(root);

        while (!f.empty()) {
            TreeNode* y = f.front();
            f.pop();
            x += eachnodesum(y);

            if (y->left != NULL) {
                f.push(y->left);
            }

            if (y->right != NULL) {
                f.push(y->right);
            }
        }

        return x;
    }
};
