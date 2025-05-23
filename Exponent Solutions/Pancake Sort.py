'''
Pancake Sort
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the 
function flip you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.

Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you 
can only use the spatula to flip some of the top pancakes in the plate. To read more about the problem, 
see the Pancake Sorting Wikipedia page.
'''

from typing import List
'''  
[1, 5, 4, 3, 2]
    m

[5, 1, 4, 3, 2]
             k

[2, 1,        ---- > 3, 4, 5]
 --->

[5, 4, 3, 2, 1]
'''

# TC: O(N^2)
# SC: O(1)
def pancake_sort(arr: List[int]) -> List[int]:
    for k in range(len(arr) -1, 0, -1):
        max_index = find_max(arr, k)
        flip(arr, max_index)
        flip(arr, k)
        
    return arr    

# TC: O(N)
# SC: O(1)
def find_max(arr, k):
    max_num, max_idx = arr[0], 0
    for i in range(k + 1):  
        if arr[i] > max_num:
            max_idx = i
            max_num = arr[i]
    return max_idx

# TC: O(N)
# SC: O(1)
def flip(arr, k):
    left = 0 
    right = k 
    while (left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    
