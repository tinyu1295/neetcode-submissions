# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        result = root

        while True:
            if val<result.val:
                if result.left == None:
                    result.left = TreeNode(val)
                    break
                else:
                    result = result.left
                    
            elif val>result.val:
                if result.right == None:
                    result.right = TreeNode(val)
                    break
                else:
                    result = result.right
                    
        return root


                

        