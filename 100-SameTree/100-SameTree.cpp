// Last updated: 4/4/2026, 12:42:33 AM
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
    vector<int> firstnd(TreeNode* p) {
        queue<TreeNode*> tm;
        vector<int> mg;
        tm.push(p);

        while (!tm.empty()) {
            TreeNode* fh = tm.front();
            tm.pop();
            mg.push_back(fh->val);

            if (fh->left != NULL) {
                tm.push(fh->left);
            }
            if (fh->right != NULL) {
                tm.push(fh->right);
            }
        }
        return mg;
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL) {
            return true;
        } else if ((p == NULL && q != NULL) || (p != NULL && q == NULL)) {
            return false;
        }

        vector<int> a = firstnd(p);
        vector<int> b = firstnd(q);

        if (a.size() != b.size()) {
            return false;
        }

        queue<TreeNode*> q1, q2;
        q1.push(p);
        q2.push(q);
        bool miltese = true;

        while (!q1.empty() && !q2.empty()) {
            TreeNode* first = q1.front();
            TreeNode* second = q2.front();
            q1.pop();
            q2.pop();

            if (first->val != second->val) {
                miltese = false;
                break;
            }

            if ((first->left != NULL && second->left == NULL) ||
                (first->left == NULL && second->left != NULL) ||
                (first->right != NULL && second->right == NULL) ||
                (first->right == NULL && second->right != NULL)) {
                miltese = false;
                break;
            }

            if (first->left != NULL) {
                q1.push(first->left);
            }
            if (first->right != NULL) {
                q1.push(first->right);
            }
            if (second->left != NULL) {
                q2.push(second->left);
            }
            if (second->right != NULL) {
                q2.push(second->right);
            }
        }
        return miltese;
    }
};
