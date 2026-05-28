# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        result = root
        while True:
            prevTree = result
            if result and key < result.val:
                result = result.left
                if result and key == result.val:
                    temp = result.left
                    prevTree.left = result.right
                    result = result.right
                    result.left = temp
                    break
            elif result and key > result.val:
                result = result.right
                if result and key == result.val:
                    temp = result.left
                    prevTree.right = result.right
                    result = result.right
                    result.left = temp
                    break
            else:
                return root
        return root


        