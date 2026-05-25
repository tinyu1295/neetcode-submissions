# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encodedKey = []

        def dfs(node):
            if not node:
                encodedKey.append("None")
                return 
            encodedKey.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(encodedKey)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        encodedKey = data.split(",")
        print(encodedKey)
        # [1,2,3,None,None] string
        self.i = 0
        def dfs():
            if encodedKey[self.i] == "None":
                self.i += 1
                return None
            node = TreeNode(int(encodedKey[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()












