from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    #empty tree
    if root is None:
        return 0
    
    #recursive case
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 + max(left_depth, right_depth)

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #base case
    if root is None:
        return None
    
    #compares values
    if root.val == p.val or root.val == q.val:
        return root
    
    #seach left and right
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    #if p and q are found in different subtrees
    if left and right:
        return root
    
    #otherwise return node found
    return left if left else right
