class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, num)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.cnt = 1
        
        
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.cnt = 1
        
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.root = None
        for n in nums:
            self.root = self.insert(self.root, n)
        

    def add(self, val: int) -> int:
        self.root = self.insert(self.root, val)
        return self.search(self.root, self.k)
        
    def search(self, node, k):
                
        while node:
            
            r_cnt = node.right.cnt if node.right else 0
            l_cnt = node.left.cnt if node.left else 0
                
            if node.cnt - l_cnt >= k > r_cnt:
                return node.val
            elif r_cnt >= k: 
                node = node.right
            else:           
                k = k - (node.cnt - l_cnt)
                node = node.left      
        

    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insert(root.right, val)
        else:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insert(root.left, val)
        root.cnt += 1
        return root

# TLE
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.root = None
        for n in nums:
            self.root = self.insert(self.root, n)
        

    def add(self, val: int) -> int:
        self.root = self.insert(self.root, val)
        return self.search(self.root, self.k)
        
    def search(self, node, k):
        if not node:
            return None
        r_cnt = node.right.cnt if node.right else 0
        l_cnt = node.left.cnt if node.left else 0
        if node.cnt - l_cnt >= k > r_cnt:
            return node.val
        elif r_cnt >= k:
            return self.search(node.right, k)
        else:
            return self.search(node.left, k - (node.cnt - l_cnt))        
        

    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        
        if root.val < val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insert(root.right, val)
        else:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insert(root.left, val)
        root.cnt += 1
        return root

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
