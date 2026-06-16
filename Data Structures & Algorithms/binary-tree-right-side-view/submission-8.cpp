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
    vector<int> rightSideView(TreeNode* root) {
        deque<TreeNode*> q;
        vector<int> result;
        int level_size;
        q.push_back(root);
        while(!q.empty()){
            level_size = q.size();
            for(int i=0;i<level_size;i++){
                TreeNode* node = q.front();
                q.pop_front();
                if(!node){
                    return result;
                }
                if(node->left){
                    q.push_back(node->left);
                }
                if(node->right){
                    q.push_back(node->right);
                }
                if(i == level_size - 1){
                    result.push_back(node->val);
                    
                }
            }
        }
        return result;
    }
};
