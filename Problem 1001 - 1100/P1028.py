import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # recursive method
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if not S:
            return None
        # get the current node level
        if S[0] != "-":
            lvl = 0
            i = 0
        else:
            lvl = 1
            i = 1
            while S[i] == "-":
                i += 1
                lvl += 1
        # get the current node value
        j = i + 1
        while j < len(S) and S[j] != "-":
            j += 1
        root = TreeNode(int(S[i:j]))
        # get the left and right branch
        lvl += 1
        k = j + 1 + lvl
        while k < len(S):
            if S[k] != "-" and S[k-lvl : k] == "".join(["-"]*lvl) and S[k-lvl-1] != "-":
                break
            k += 1
        # no right branch
        if k == len(S):
            root.left = self.recoverFromPreorder(S[j:])
        else:
            root.left = self.recoverFromPreorder(S[j:k-lvl])
            root.right = self.recoverFromPreorder(S[k-lvl:])
        return root
                    
    def recoverFromPreorder_1(self, S: str):
        stack = []
        i = 0
        while i < len(S):
            level = 0
            val = ""
            while i < len(S) and S[i] == '-':
                level += 1
                i += 1
            while i < len(S) and S[i] != '-':
                val += S[i]
                i += 1
            # make sure the current level equals len(stack)
            while len(stack) > level:
                stack.pop()
            node = TreeNode(int(val))
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]

S = "1-2--3--4-5--6--7"
S = "1-2--3---4-5--6---7"
sol = Solution()
t = sol.recoverFromPreorder(S)
print(t)