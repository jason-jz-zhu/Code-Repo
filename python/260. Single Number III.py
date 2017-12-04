class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []

        tmp = 0
        for num in nums:
            tmp ^= num

        flag = tmp & (~(tmp - 1))
        a = b = 0
        for num in nums:
            if num & flag == 0:
                a ^= num
            else:
                b ^= num

        return [a, b]

# flag = tmp & (~(tmp - 1))

# public static int f(int num){
#     int times = 0;
#     while(num > 0){
#         if(num % 2 == 1){
#             break;
#         }
#         times++;
#         num = num >> 1;
#     }
#
#     return 1 << times;
# }
