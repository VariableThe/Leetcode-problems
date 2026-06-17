class Solution(object):
    def buildTree(self, inorder, postorder):
        inorder_index_map = {val: i for i, val in enumerate(inorder)}

        def build(left, right):
            if left > right:
                return None

            root_value = postorder.pop()
            root = TreeNode(root_value)

            inorder_idx = inorder_index_map[root_value]

            root.right = build(inorder_idx + 1, right)
            root.left = build(left, inorder_idx - 1)

            return root

        return build(0, len(inorder) - 1)
