# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 0
        lheight=height(root.left)
        rheight=height(root.right)
        Left_diameter=self.diameterOfBinaryTree(root.left)
        Right_diameter=self.diameterOfBinaryTree(root.right)
        return max(lheight+rheight,max(Left_diameter,Right_diameter))
                   
def height(root):
    if root is None:
        return 0
    current=root
    q=[]
    q.append(root)
    height=0
    while True:
        nodeCount=len(q)
        if nodeCount==0:
            return height
        height+=1

        while nodeCount>0:
            current=q.pop(0)
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
            nodeCount-=1
            