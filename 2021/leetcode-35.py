
from typing import List
import pytest


class Solution:
    """35. 搜索插入位置
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

    你可以假设数组中无重复元素。

    示例 1:

    输入: [1,3,5,6], 5
    输出: 2
    示例 2:

    输入: [1,3,5,6], 2
    输出: 1
    示例 3:

    输入: [1,3,5,6], 7
    输出: 4
    示例 4:

    输入: [1,3,5,6], 0
    输出: 0

    我的解法是顺序执行的，并且偷懒的使用了 enumerate 这个函数，其实还是尽量少使用这种方式

    其实本题的主要考查点是二分查找，这个才是最佳的解法，可以增加效率
    """
    def solution(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v >= target :
                return i
            if i == (len(nums) -1):
                return i + 1

class TestSolution:
    test_data_one = (([1,3,5,6], 5), 2)
    test_data_two = (([1,3,5,6], 2), 1)
    test_data_three = (([1,3,5,6], 7), 4)
    test_data_four = (([1,3,5,6], 0), 0)

    

    @pytest.mark.parametrize('input_data, assert_data', [test_data_one, test_data_two, test_data_three, test_data_four])
    def test_solution(self, input_data, assert_data):
        assert Solution().solution(input_data[0], input_data[1]) == assert_data
