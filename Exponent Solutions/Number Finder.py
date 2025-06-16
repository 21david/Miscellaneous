'''
https://www.tryexponent.com/courses/algorithms/number-finder
''']

from typing import List

def find_first(array: List[int], num: int) -> int:
    if len(array) == 0:
        return -1
    elif array[0] == num:
        return 0

    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if array[mid] < num:
            lo = mid + 1
        elif array[mid] > num or (array[mid] == num and array[mid - 1] == num): 
            hi = mid - 1
        elif array[mid] == num and array[mid - 1] != num:
            return mid
    
    return -1
        
 
# debug your code below   
print(find_first([200, 200, 200, 200, 500, 500, 500], 200))
print(find_first([500], 200))

'''
Takeaways:
Interviewer may be throwing you off, ask questions like "Is the array sorted"
For this question, ask  if there's always only 200 and 500, or other numbers, including more than 2 distinct numbers.
I assumed only 200 and 500 despite the function taking in any array and any num.
'''
