
from typing import List
import pytest


class Solution:
    """
    17. 电话号码的字母组合

    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
    ##########################################################################

    示例 1：
    输入：digits = "23"
    输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]


    示例 2：
    输入：digits = ""
    输出：[]

    示例 3：
    输入：digits = "2"
    输出：["a","b","c"]
    ##########################################################################
    """
    def solution(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        for i in digits:
            for i in d[i]:



class TestSolution:
    test_data_one = ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"])
    test_data_two =  ("", [])

    @pytest.mark.parametrize('input_data, assert_data', [test_data_one, test_data_two])
    def test_solution(self, input_data, assert_data):
        assert Solution().solution(input_data) == assert_data
