# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if not root:
                return []
            q = collections.deque()
            q.append(root)
            result = []
            # For each layer
            while q:
                qLen = len(q)
                currLvl = []
                # For each node
                for _ in range(qLen):
                    node = q.popleft()
                    currLvl.append(node.val)
                    # Check children before adding
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                if currLvl:
                    result.append(currLvl)
            
            return result
            






