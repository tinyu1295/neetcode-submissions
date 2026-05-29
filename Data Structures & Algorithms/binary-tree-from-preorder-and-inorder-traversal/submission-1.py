# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre[1,2,3,4] 
        # inor[2,1,3,4]

        if not preorder and not inorder:
            return None
        
        root = TreeNode(preorder[0])
        midPoint = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:midPoint+1], inorder[:midPoint])
        root.right = self.buildTree(preorder[midPoint+1:], inorder[midPoint+1:])

        return root
