from typing import List

'''  
Visual example:
                              [     ]
                           [    ]
                 [     ]
             [        ]
         [ ]
   [  ]
[            ]

[           ]
[       ]
[         ]


Algorithm:
1. Sort by only the starting point
2. For each following interval, check if the next interval starts at the current end, 
   repeat until it doesn't, and add the current interval to the final answer

TC: O(NlogN)
SC: O(N)
'''
def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    length = len(intervals)
    intervals.sort(key = lambda interval: interval[0])
    output = []

    i = 0
    while i < length:
        start, end = intervals[i]

        j = i + 1
        while j < length:
            next_start, next_end = intervals[j]

            if next_start <= end:
                end = max(end, next_end)
            else:
                break

            j += 1

        i = j
        output.append([start, end])

    return output


'''
Better solution without nested loops
TC: O(NlogN)
SC: O(N)
'''
def mergeIntervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    
    length = len(intervals)
    intervals.sort(key = lambda interval: interval[0])

    # Initialize the output list with the first interval
    output = [intervals[0]]

    for i in range(1, len(intervals)):
        prev_interval = output[-1]
        curr_interval = intervals[i]

        if prev_interval[1] >= curr_interval[0]:
            prev_interval[1] = max(prev_interval[1], curr_interval[1])
        else:
            output.append(curr_interval)

    return output
    

# debug your code below
print(mergeIntervals([[1,4]]))
print(mergeIntervals([[1,4],[4,5]]))  # =>  [[1,5]]
print(mergeIntervals([[1,3], [2,6], [8,10], [15,18]]))
