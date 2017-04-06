import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        nums.sort()
        nums.reverse()
        return nums[:k]


import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        heapq.heapify(nums)
        top_k = heapq.nlargest(k, nums)
        top_k.sort()
        topk.reverse()
        return top_k
