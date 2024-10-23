# https://www.tryexponent.com/practice/prepare/time-planner
# Solution written on September 27, 2024
from typing import List
def meeting_planner(slotsA: List[List[int]], slotsB: List[List[int]], dur: int) -> List[int]:
    a = b = 0
    A, B = len(slotsA), len(slotsB)

    while a < A and b < B:
        a_interval = slotsA[a]
        b_interval = slotsB[b]

        overlap = get_overlap(*a_interval, *b_interval)
        if overlap and (overlap[1] - overlap[0] >= dur):
            return [overlap[0], overlap[0] + dur]
        else:
            if a_interval[1] < b_interval[1]:
                a += 1
            elif a_interval[1] == b_interval[1]:
                a += 1
                b += 1
            else:
                b += 1

    return []

def get_overlap(a_left, a_right, b_left, b_right):
    start = max(a_left, b_left)
    end = min(a_right, b_right)
    
    if start < end:
        return [start, end]
    return None



# Solution written on October 22, 2024
from typing import List
def meeting_planner(slotsA: List[List[int]], slotsB: List[List[int]], dur: int) -> List[int]:
  # Two pointers
  a = b = 0
  A, B = len(slotsA), len(slotsB)
  while a < A and b < B:
    overlap, length = get_overlap(slotsA[a], slotsB[b])

    if overlap and length >= dur:
      return [overlap[0], overlap[0] + dur]

    else:
      # Check which one is behind
      if slotsA[a][1] <= slotsB[b][1]:
        # slotsA is behind
        a += 1
      elif slotsB[b][1] <= slotsA[a][1]:
        b += 1

  return []

def get_overlap(sA, sB):
  a_s, a_e = sA
  b_s, b_e = sB

  start = max(a_s, b_s)
  end = min(a_e, b_e)

  if start < end:
    return [start, end], end - start
  
  return None, None
