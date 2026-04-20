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
    int maxDepth(TreeNode* root) {
        if (!root) return 0;
        return 1 + max_depth(root);
    }
    int max_depth(TreeNode*& root){
        if (!root) return 0;
        int leftdepth = 0;
        int rightdepth = 0;
        if (root->left){
            leftdepth = 1 + max_depth(root->left);
        }
        if (root->right){
            rightdepth = 1 + max_depth(root->right);
        }

        if (leftdepth > rightdepth) return leftdepth;
        return rightdepth;


    }
};
