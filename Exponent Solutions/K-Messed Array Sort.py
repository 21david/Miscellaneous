from typing import List
from heapq import heapify, heappush as push, heappop as pop

'''  
Use a sliding window with a heap. The heap stores k+1 elements
at a time, starting with the first k+1 elements. The first window
takes the minimum of the k+1, which is guaranteed to be the first
element in the whole array since it can only be k distance away.
Then we push the next element into the heap and repeat for every
position of the window. At the end, drain the remaining elements
in the heap.

TC: O(N log k)
SC: O(k)
'''
def sort_k_messed_array(arr: List[int], k: int) -> List[int]:
    N = len(arr)
    heap = heapify([arr[i] for i in range(k+1)])
    answer = []

    # Sliding window
    for i in range(k + 1, N):
        answer.append(pop(heap))
        push(heap, arr[i])

    # Sort remaining k elements in heap
    while heap:
        answer.append(pop(heap))
    
    return answer


# debug your code below
print(sort_k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))

'''  
Sample run, if we swapped in the input array:
This may be possible by storing and updating indices
along with the actual numbers in the heap.
[1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2
[1, 2, 5, 4, 3, 7, 8, 6, 10, 9], 2
[1, 2, 3, 4, 5, 7, 8, 6, 10, 9], 2
[1, 2, 3, 4, 5, 7, 8, 6, 10, 9], 2
[1, 2, 3, 4, 5, 7, 8, 6, 10, 9], 2
[1, 2, 3, 4, 5, 6, 8, 7, 10, 9], 2
...

'''
