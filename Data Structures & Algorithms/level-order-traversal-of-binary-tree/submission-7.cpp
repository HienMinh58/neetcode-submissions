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
#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        vector<vector<int>> results;
        
        int level_size;
        while(!q.empty()) {
            
            vector<int> level;
            level_size = q.size();
            
            for(int i=0;i<level_size;i++){
                TreeNode* node = q.front();
                q.pop();
                if(!node){
                    return results;
                }
                if(node->left){
                    q.push(node->left);
                }
                if(node->right){
                    q.push(node->right);
                }
                level.push_back(node->val);
            }
            results.push_back(level);
        }   
        return results;
    }
};
