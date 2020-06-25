Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.

Python3 program:

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        return self.bstFromPreorderandinorder(preorder,inorder)
    
    def bstFromPreorderandinorder(self, preorder,inorder):
        
        lengthpre = len(preorder)
        lengthin = len(inorder)
        
        if lengthpre != lengthin or preorder == None or inorder == None or lengthpre == 0:
            return None
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)
        
        root.left = self.bstFromPreorderandinorder(preorder[1:rootindex + 1],inorder[:rootindex])
        
        root.right = self.bstFromPreorderandinorder(preorder[rootindex + 1:],inorder[rootindex + 1:])
        
        return root
    
