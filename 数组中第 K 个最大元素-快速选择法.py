class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        piv = nums[0]  # 取第一个为初始数
        left = [i for i in nums if i > piv]  # 大的放左边
        mid = [i for i in nums if i == piv]  # 相同的放中间
        right = [i for i in nums if i < piv]  # 小的放右边

        if len(left) >= k:  # 如果大的数超过了 K，就在大的列表里递归
            return self.findKthLargest(left, k)
        elif len(left) < k and len(left) + len(mid) >= k:
            return piv
        else:
            return self.findKthLargest(right, k - len(left) - len(mid))
