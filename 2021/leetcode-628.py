from typing import List
import pytest


class Solution:
    """
    628. 三个数的最大乘积

    给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

    示例 1：
    输入：nums = [1,2,3]
    输出：6

    示例 2：
    输入：nums = [1,2,3,4]
    输出：24

    示例 3：
    输入：nums = [-1,-2,-3]
    输出：-6

    提示：

    3 <= nums.length <= 104
    -1000 <= nums[i] <= 1000

    """
    def solution(self, nums: List[int]) -> int:
        nums.sort()
        max1 = nums[-1] * nums[-2] * nums[-3]
        max2 = nums[0] * nums[1] * nums[-1]
        return max1 if max1 > max2 else max2


class TestSolution:
    test_data_one = ([1,2,3], 6)
    test_data_two =  ([1,2,3,4], 24)
    test_data_three =  ([-1,-2,-3], -6)

    @pytest.mark.parametrize('input_data, assert_data', [test_data_one, test_data_two, test_data_three])
    def test_solution(self, input_data, assert_data):
        assert Solution().solution(input_data) == assert_data
