class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = []
        current_interval = intervals[0]
        result.append(current_interval)
        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            last_merge_end = current_interval[1]
            if current_start<=last_merge_end:
                new_end = max(current_end, last_merge_end)
                current_interval[1] = new_end
            else:
                current_interval = [current_start, current_end]
                result.append(current_interval)
        return result