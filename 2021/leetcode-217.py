from typing import List
import pytest


class Solution:
    """给数组，寻找相同的数字
    1. 使用 python 的 set 这个数据结构，可以完美解决
    2. 排序，然后遍历，记住前一个数据，每次对比就好了
    3. 使用 dict 进行统计！

    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        raw_length = len(nums)
        set_length = len(set(nums))
        return True if raw_length != set_length else False
        # return len(nums) == len(set(nums)) 这种写法更加好，也更加抽象


class TestSolution:
    test_data_one = ([1, 2, 3, 1], True)
    test_data_two = ([1, 2, 3, 4], False)
    test_data_three = ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)

    @pytest.mark.parametrize(
        'input_data, assert_data', [test_data_one, test_data_two, test_data_three]
    )
    def test_solution(self, input_data, assert_data):
        assert Solution().containsDuplicate(input_data) == assert_data
