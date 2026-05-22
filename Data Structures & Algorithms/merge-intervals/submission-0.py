class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(n logn)
        intervals.sort(key=lambda x: x[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            endPoint = output[-1][1]

            if endPoint >= start:
                output[-1][1] = max(endPoint, end)
            else:
                output.append([start, end])
        return output