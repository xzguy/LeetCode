class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # traverse the tree in-order first
    # then check the list is sorted or not
    def isValidBST_1(self, root: TreeNode) -> bool:
        if not root:
            return True
        tn_l = self.DFS_append(root, [])
        return all(tn_l[i] < tn_l[i+1] for i in range(len(tn_l)-1))
        
    def DFS_append(self, root: TreeNode, tree_node_list):
        if not root:
            return
        self.DFS_append(root.left, tree_node_list)
        tree_node_list.append(root.val)
        self.DFS_append(root.right, tree_node_list)
        return tree_node_list

    # traverse the tree with upper and lower limits
    # once violation happens, return False
    def isValidBST_2(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.DFS_valid(root.left, None, root.val) and \
            self.DFS_valid(root.right, root.val, None)

    def DFS_valid(self, root: TreeNode, t_min, t_max) -> bool:
        if not root:
            return True
        if t_min is not None and root.val <= t_min:
            return False
        if t_max is not None and root.val >= t_max:
            return False
        return self.DFS_valid(root.left, t_min, root.val) and \
            self.DFS_valid(root.right, root.val, t_max)


tree = TreeNode(5)
tree.left = TreeNode(1)
tree.right = TreeNode(4)
tree.right.left = TreeNode(3)
tree.right.right = TreeNode(6)

sol = Solution()
print(sol.DFS_append(tree, []))
print(sol.isValidBST_1(tree))

t1 = TreeNode(0)
t1.right = TreeNode(-1)

print(sol.isValidBST_2(t1))
