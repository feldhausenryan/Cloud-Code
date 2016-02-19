#Function answer(intervals)
#Input : A list of pairs e.g. (int) [[1,2], [2,4]]
#Output: (int) The coverage of the input eg 2-1 + 4-2 = 3 for the above input
#Method: Take the input and sort it (primary = first) (secondary = last).
#Then iterate through the list and keep track of the current interval and the sum of previous intervals
#Runtime: O(n) (Linear)
def answer(intervals):
    length_intervals = len(intervals)
    #catch a list of size zero
    if (length_intervals == 0):
        return int(0)
    #cath a list of size one
    if (length_intervals == 1):
        return int(intervals[0][1]-intervals[0][0])
    #sort the list
    intervals.sort()
    #helper variables and initialization of the first interval
    current_interval_start = intervals[0][0]
    current_interval_end = intervals[0][1]
    running_interval_sum = 0
    #loop through the list excluding the first term
    for pair in intervals[1:]:
        #if the start of the next interval lies beyond the end of the current one,
        #sum up the current interval and start a new one
        if (pair[0] > current_interval_end):
            #summing up...
            running_interval_sum += current_interval_end - current_interval_start
            #starting a new one...
            current_interval_start = pair[0]
            current_interval_end = pair[1]
            continue
        #if the start of the next intervals lies within the end of the current one,
        #extend the interval
        else:
            current_interval_end = max(current_interval_end, pair[1])
            continue
    #sum up the current last interval
    running_interval_sum += current_interval_end - current_interval_start
    #return the answer
    return int(running_interval_sum)
