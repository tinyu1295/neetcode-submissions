class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Step 1: search for node
        parent = None
        curr = root

        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:
            return root  # key not found

        # Step 2: if node has two children, swap with inorder successor
        if curr.left and curr.right:
            # find smallest in right subtree
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left

            # replace current value
            curr.val = succ.val
            # now delete successor instead
            curr = succ
            parent = succ_parent

        # Step 3: delete node with at most one child
        child = curr.left if curr.left else curr.right

        # if deleting root
        if not parent:
            return child

        if parent.left == curr:
            parent.left = child
        else:
            parent.right = child

        return root
