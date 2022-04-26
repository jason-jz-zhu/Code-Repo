class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def helper(node):
            nonlocal first, last
            
            if not node:
                return
            helper(node.left)
            if last:
                node.left = last
                last.right = node
            else:
                first = node
            
            last = node
            helper(node.right)
        
        
        if not root:
            return None
        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first
    
    
 class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if root is None:
            return None


        stack = []
        last, first = None, None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if last:
                    root.left = last
                    last.right = root
                else:
                    first = root
                last = root
                root = root.right
        last.right = first
        first.left = last
        return first
