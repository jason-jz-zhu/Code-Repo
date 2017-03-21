"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        if root is None:
            return '{}'
        q = collections.deque([root])
        result = [root]
        while q:
            head = q.popleft()
            result.append(head.left)
            result.append(head.right)
            if head.left:
                q.append(head.left)
            if head.right:
                q.append(head.right)
        while result[-1] is None:
            result.pop()

        return '{%s}' % ','.join([str(node.val) if node else '#' for node in result])

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if data == '{}':
            return None
        s_array = data[1:-1].split(',')
        root = TreeNode(int(s_array[0]))
        q = [root]
        is_left_child = True
        index = 0

        for s in s_array[1:]:
            if s is not '#':
                node = TreeNode(int(s))
                if is_left_child:
                    q[index].left = node
                else:
                    q[index].right = node
                q.append(node)
            if not is_left_child:
                index += 1
            is_left_child = not is_left_child
        return root
