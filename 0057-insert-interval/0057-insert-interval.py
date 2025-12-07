class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)

        # newInterval[0] is start, newInterval[1] end

        for i in range(n):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)

                return result + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        result.append(newInterval)
        return result