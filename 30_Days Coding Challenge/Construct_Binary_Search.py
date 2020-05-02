# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        length=len(preorder)
        head=TreeNode(preorder[0])
        previous=None
        
        for i in range(1,length):
            new_node=TreeNode(preorder[i])
            value=preorder[i]
            current=head
            flag=-1
            while current:
                if value > current.val:
                    previous=current
                    current=current.right
                    flag=0
                elif value < current.val:
                    previous=current
                    current=current.left
                    flag=1
                else:
                    previous=current
                    current=current.left
                    flag=1
                    
            if flag == 1:
                previous.left=new_node
            else:
                previous.right=new_node
                
        return head
            
                    