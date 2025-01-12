# https://www.tryexponent.com/practice/f65f9f2b-5a1e-4e5c-a0b7-08af7d6b28fc
# Basically Two Sum
def get_indices_of_item_weights(arr: List[int], limit: int) -> List[int]:
    index_dict = {num : i for i, num in enumerate(arr)}
    ans = []
    
    for i, num in enumerate(arr):
        complement = limit - num
        if complement in index_dict:
            j = index_dict[complement]
            if i != j:
                ans = [i, j] if i > j else [j, i]

    return ans
