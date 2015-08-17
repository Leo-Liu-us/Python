# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
        #empty list
        if ((len(preorder) == 0) or (len(inorder) == 0)):
            return None
        #leaf nodes
        elif ((len(preorder) == 1) or (len(inorder) == 1)):
            return TreeNode(preorder[0])
        #non-leaf nodes
        else:
            rootVal = preorder[0]
            #construct root
            root = TreeNode(rootVal)
            
            #partion preorder and inorder
            partionIdx = inorder.index(rootVal)
            #partion inorder
            leftInorder = inorder[0 : partionIdx]
            rightInorder = inorder[partionIdx + 1:]
            #partion preorder
            leftPreorder = preorder[1 : 1 + len(leftInorder)]
            rightPreorder = preorder[1 + len(leftPreorder):]
            
            #construct left subtree recursively
            root.left = self.buildTree(leftPreorder, leftInorder)
            #construct right subtree recursively
            root.right = self.buildTree(rightPreorder, rightInorder)
            
            return root