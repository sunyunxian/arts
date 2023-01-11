from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        people_counter: dict = {}
        for i in logs:
            birth, death = i[0], i[1]
            for year in range(birth, death):
                if year not in people_counter:
                    people_counter[year] = 1
                else:
                    people_counter[year] += 1
            # 一开始用了这个逻辑，也就是 death 的年份也进行了计算，这样就会导致某些年份是负数
            # 实际上某一年的人数是不可能为负数的，所以这段忽略掉是合适的
            # 因为本身 death 就没有 +1，所以就不能直接减一的，如果上面用了 death + 1
            # 那么这段代码是可以的
            # if death not in people_counter:
            #     people_counter[death] = -1
            # else:
            #     people_counter[death] -= 1
        print(people_counter)
        max_year: int = 0
        max_people: int = 0
        for year, people in people_counter.items():
            if people > max_people:
                max_year, max_people = year, people
            elif people == max_people and max_year == 0:
                max_year, max_people = year, people
            elif people == max_people and max_year > year:
                max_year, max_people = year, people
            else:
                pass
        print(max_year, max_people)
        return max_year


if __name__ == '__main__':
    logs = [[1993, 1999], [2000, 2010]]
    print(Solution().maximumPopulation(logs))
    logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
    print(Solution().maximumPopulation(logs))
    logs = [
        [2044, 2049],
        [2020, 2044],
        [1958, 2024],
        [1990, 2007],
        [1962, 1980],
        [1997, 2050],
        [2005, 2033],
        [2028, 2035],
        [2028, 2036],
        [2035, 2040],
        [2022, 2035],
        [1971, 2047],
        [1967, 1994],
        [1952, 1976],
        [1967, 2030],
        [2014, 2045],
        [2039, 2049],
        [1951, 2001],
        [2003, 2008],
        [1991, 2001],
        [1995, 2002],
        [2039, 2043],
        [2036, 2048],
        [1960, 1970],
        [2015, 2048],
        [2048, 2049],
        [1979, 1989],
        [2013, 2039],
        [2048, 2050],
        [1969, 2031],
        [1971, 2045],
        [1995, 2024],
        [1981, 2028],
        [2016, 2027],
        [2036, 2039],
        [1954, 2021],
        [2033, 2040],
        [2040, 2041],
        [1973, 1980],
        [1968, 1989],
        [2022, 2038],
        [1954, 1961],
        [2047, 2049],
        [2012, 2036],
        [2039, 2045],
        [2044, 2048],
        [1957, 1989],
        [2027, 2038],
        [1978, 2026],
        [2025, 2037],
        [2024, 2041],
        [1989, 2026],
        [2023, 2026],
        [1983, 1992],
        [2038, 2049],
        [1951, 1989],
        [2021, 2048],
        [2027, 2036],
        [2000, 2029],
        [2014, 2032],
        [2010, 2022],
        [2027, 2038],
        [1977, 1989],
        [1982, 2022],
        [1954, 2048],
        [2034, 2045],
        [2022, 2045],
        [1977, 2018],
        [2023, 2033],
        [1976, 2006],
        [2019, 2045],
        [1996, 2028],
        [1975, 2031],
        [1988, 2043],
        [2006, 2048],
        [2011, 2047],
        [2019, 2039],
        [2012, 2039],
        [2011, 2033],
        [1952, 1973],
        [1985, 2031],
        [1961, 2018],
        [1980, 2050],
        [1950, 1976],
        [2031, 2039],
        [1996, 2002],
        [2016, 2029],
        [1988, 2009],
        [1970, 2008],
        [1956, 1971],
        [1956, 2049],
        [1959, 1995],
        [2021, 2033],
        [2000, 2023],
        [1990, 2033],
        [1979, 2017],
        [1991, 2006],
        [2005, 2034],
        [2015, 2038],
        [2047, 2048],
    ]
    print(Solution().maximumPopulation(logs))
