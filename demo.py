# -*- coding: utf-8 -*-
# LeetCode 88: Merge Sorted Array - 最精简版本

def merge(nums1, m, nums2, n):
    """合并两个有序数组到nums1中"""
    # 从后往前合并，避免覆盖
    last = m + n - 1
    i, j = m - 1, n - 1
    
    while j >= 0:  # 只要nums2还有元素就继续
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[last] = nums1[i]
            i -= 1
        else:
            nums1[last] = nums2[j]
            j -= 1
        last -= 1

# 测试
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge(nums1, 3, nums2, 3)
print(f"结果: {nums1}")  # [1, 2, 2, 3, 5, 6]

