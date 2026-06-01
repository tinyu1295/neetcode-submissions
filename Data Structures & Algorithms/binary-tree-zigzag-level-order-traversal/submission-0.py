# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        queue = deque([root])
        res = []
        l_to_r = True

        while queue:
            lvl = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if l_to_r:
                    lvl.append(node.val)
                else:
                    lvl.appendleft(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(list(lvl))
            l_to_r = not l_to_r

        return res

        