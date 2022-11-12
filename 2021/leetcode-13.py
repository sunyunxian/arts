import pytest


class Solution:
    def romanToInt(self, s: str) -> int:
        """13. 罗马数字转整数

        本地的关键在于能否正确的理解这个题目，这个题目其实表达是：s 中元素，比右边小的就 -，比右边大的就 +，理清楚这一点基本上就可以解决了

        1. 在处理 length 有技巧，也就是最后一个需要判断进行特殊处理，不然会越界 out of index
        2. 尽量不使用 `if i < len(s) -1  and dic[s[i]] < dic[s[i+1]]` 付出的代价是每次都会增加判断，而这一步可以放到最后解决
           能避免多一次计算，时间复杂度最低！
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 0
        for i in range(len(s)):
            if i < len(s) - 1 and dic[s[i]] < dic[s[i + 1]]:
                count -= dic[s[i]]
            else:
                count += dic[s[i]]
        return count

    def romanToIntTwo(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 0
        length = len(s) - 1
        for i in range(length):
            if dic[s[i]] < dic[s[i + 1]]:
                count -= dic[s[i]]
            else:
                count += dic[s[i]]
        return count + dic[s[length]]


class TestRomanToInt:
    test_data_one = ('II', 2)
    test_data_two = ('XII', 12)

    @pytest.mark.parametrize('roman_data, assert_data', [test_data_one, test_data_two])
    def test_comment(self, roman_data, assert_data):
        assert Solution().romanToInt(roman_data) == assert_data

    test_data_one = ('MCMXCIV', 1994)
    test_data_two = ('CMXCIX', 999)

    @pytest.mark.parametrize('roman_data, assert_data', [test_data_one, test_data_two])
    def test_special(self, roman_data, assert_data):
        assert Solution().romanToInt(roman_data) == assert_data


if __name__ == '__main__':
    print(Solution().romanToInt('XII'))
