# https://leetcode.com/problems/merge-intervals/
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort intervals  by start_i
        intervals.sort()
        
        # instantiate solution
        intervals_merged = []
        
        for i in intervals:
            if intervals_merged == [] or i[0] > intervals_merged[-1][1]:
                intervals_merged.append(i)
            else:
                intervals_merged[-1][1] = max(intervals_merged[-1][1], i[1])
                
        return intervals_merged
        
        
        
        
    def mergeBad(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # instantiate output and sliding window indexes
        non_overlapping_intervals = []
        i=0
        j=0
        
        # make sure intervals is sorted by start
        intervals.sort()
        
        # slide the window
        while i < len(intervals):
            # move i to next index, 
            # in case where we merged indexes in prev iteration
            if i < j:
                i+=1
                continue
            
            # get sub window starting range
            start_i = intervals[i][0]
            end_i = intervals[i][1]
            
            # if subwindow starting on final element, add it and break
            if i == len(intervals)-1:
                non_overlapping_intervals.append([start_i, end_i])
                break
            
            # get sub window ending range
            j=i+1
            start_j = intervals[j][0]
            
            if start_j > end_i:
                non_overlapping_intervals.append([start_i, end_i])
            else:
                while (start_j <= end_i) & (j < len(intervals)):
                    # if subwindow ending on final element, add it and break
                    if j == len(intervals)-1:
                        non_overlapping_intervals.append([start_i, intervals[j][1]])
                        break
                
                    j+=1
                    start_j = intervals[j][0]
                    
                non_overlapping_intervals.append([start_i, intervals[j-1][1]])
 
            i+=1    
        return non_overlapping_intervals
