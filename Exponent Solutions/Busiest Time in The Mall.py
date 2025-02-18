from typing import List
"""
TC: O(N)
SC: O(1)
"""
def find_busiest_period(data: List[List[int]]) -> int:
    if len(data) == 1:
        return data[0][0]

    N = len(data)
    current_net = 0
    max_net = -float('inf')
    busiest_time = -1
    prev_time = -1

    for i in range(N):
        time, count, status = data[i]

        if time != prev_time:
            # We have gone through all arrays of the last timestamp, now check
            # if the overall change is a new record
            if current_net > max_net:
                max_net = current_net
                busiest_time = prev_time

            # Start over with the next distinct timestamp
            prev_time = time

        if status == 1:
            current_net += count
        else:
            current_net -= count

    # Check for the last distinct timestamp
    if current_net > max_net:
        max_net = current_net
        busiest_time = time

    return busiest_time
