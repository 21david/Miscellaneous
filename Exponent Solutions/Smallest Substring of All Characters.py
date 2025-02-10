from typing import List

"""
TC: O(len(str))
SC: O(len(arr))
"""
import math
def get_shortest_unique_substring(arr: List[str], str: str) -> str:
    if len(str) < len(arr):
        return ''

    N = len(str)
    counts = {}
    min_len = math.inf
    l = r = l_min = r_min = 0
    arr_set = set(arr)

    while r <= N:
        if len(counts) < len(arr):
            # Expand from right
            if r == N:
                # This is in the case the shortest substring is at the end.
                # This will let it shrink in the else below as much as possible.
                break
            curr_letter = str[r]
            r += 1
            if curr_letter in arr_set:
                counts[curr_letter] = counts.get(curr_letter, 0) + 1
            
        else:
            # Shrink from left
            curr_letter = str[l]
            if curr_letter in arr_set:
                counts[curr_letter] -= 1
                if counts[curr_letter] == 0:
                    del counts[curr_letter]
            
            l += 1

        if len(counts) == len(arr) and r - l + 1 < min_len: 
            min_len = r - l + 1
            l_min = l
            r_min = r

    return str[l_min:r_min] if min_len != math.inf else ''

print(get_shortest_unique_substring(['x'], 'x'))
print(get_shortest_unique_substring(['x','y','z'], 'xyyzyzyx'))
