
from typing import List
import pytest


class Solution:
    """

    """
    def solution(self, s: str) -> int:
        i = 0
        result = 0
        if s[i] == s[i+1]:
            pass





class TestSolution:
    test_data_one = ("abcabcbb", 3)
    test_data_two =  ("bbbbb", 1)

    @pytest.mark.parametrize('input_data, assert_data', [test_data_one, test_data_two])
    def test_solution(self, input_data, assert_data):
        assert Solution().solution(input_data) == assert_data
