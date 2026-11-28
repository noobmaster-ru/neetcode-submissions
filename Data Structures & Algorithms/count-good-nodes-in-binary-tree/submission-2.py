# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, root: TreeNode, number_good: int, maxElem: int):
        right_val = 0
        left_val = 0
        if root.val >= maxElem:
            maxElem = root.val
            number_good += 1
        
        if root.left is not None:
            left_val = self.traverse(root.left, 0, maxElem)
        
        if root.right is not None:
            right_val = self.traverse(root.right, 0 , maxElem)
        
        if root.right is None and root.left is None:
            return number_good

        return left_val + number_good + right_val
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.traverse(root, 0, root.val)