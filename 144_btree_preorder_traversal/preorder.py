# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        s = []
        result = []
        #init
        if root:
            s.append(root)
            
        while len(s) > 0:
            temp = s.pop()
            result.append(temp.val)
            
            if temp.right:
                s.append(temp.right)
            if temp.left:
                s.append(temp.left)
                
        return result