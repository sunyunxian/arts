
from typing import List
import pytest


class Solution:
    """
    有效字符串需满足：

        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
 
    最好的方法是用 stack 来解决，当遇到左括号的时候入栈，右括号的时候，判断是否是对应的，
    如果对应那么 pop，如果不对应，那么直接就是错误了，到最后看一下这个 stack，如果是空，那么就返回 True
    """
    def isValid(self, s: str) -> bool: 
        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in d:
               stack.append(i)
            else:
                if len(stack) == 0:
                    return False 
                elif d[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return False if stack else True


class TestSolution:
    test_data_one = ("()", True)
    test_data_two =  ("()[]{}", True)

    test_data_three =  ("(]", False)
    test_data_four =  ("([)]", False)

    @pytest.mark.parametrize('input_data, assert_data', [test_data_one, test_data_two, test_data_three, test_data_four])
    def test_solution(self, input_data, assert_data):
        assert Solution().isValid(input_data) == assert_data
