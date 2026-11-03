
def can_attend_meetings(intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


# Example
meetings = [[0, 30], [5, 10], [15, 20]]

if can_attend_meetings(meetings):
    print("All meetings can be attended")
else:
    print("Meetings overlap")
