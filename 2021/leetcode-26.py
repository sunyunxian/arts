from typing import List
import pytest


class Solution:
    """26. 删除排序数组中的重复项

    本题使用双指针的解法，也就是 slow 和 fast 两个指针
    当 fast 在移动过程中遇到不同的 slow 指针值，将 fast 的值赋值给 slow + 1 的 index 位置

    """

    def remove_duplicates(self, nums: List[int]) -> int:

        slow = 0
        for i in range(1, len(nums)):
            if nums[slow] != nums[i]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1


class TestSolution:
    test_data_one = ([1, 1, 2], 2)
    test_data_two = ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)

    @pytest.mark.parametrize('input_data, assert_data', [test_data_one, test_data_two])
    def test_remove_duplicates(self, input_data, assert_data):
        assert Solution().remove_duplicates(input_data) == assert_data
