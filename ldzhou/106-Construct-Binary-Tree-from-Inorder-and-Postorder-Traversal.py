class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if(inorder.empty()){
            return NULL;
        }
        return build(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1);
    }
    
    TreeNode * build(vector<int>& inorder, int start1, int end1, vector<int>& postorder, int start2, int end2){
        if(start1 > end1){
            return NULL;
        }
        TreeNode* root = new TreeNode(postorder[end2]);
        for(auto i = start1; i <= end1; i++){
            if(inorder[i] == root->val){
                root->left = build(inorder, start1, i - 1, postorder, start2, i - 1 - start1 + start2);
                root->right = build(inorder, i + 1, end1, postorder, i - start1 + start2, end2 - 1);
                return root;
            }
        }
        return root;
    }
};
