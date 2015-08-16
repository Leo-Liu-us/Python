# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        #leaf
        if root.left is None and \
        root.right is None:
            if root.val == sum:
                return True
        #search in the left subtree
        if self.hasPathSum(root.left, sum - root.val):
            return True
        else:
            return self.hasPathSum(root.right, sum - root.val)