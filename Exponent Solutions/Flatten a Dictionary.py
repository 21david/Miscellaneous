# Mock interview Jan 2 2025
from typing import Dict, Union

DeepNestedDict = Dict[str, Union[str, 'DeepNestedDict']]

# Time complexity: O(N)
# Auxiliary space complexity: O(L)
# Output space complexity: O(N)
# N = number of key-value pairs
# L = number of levels
'''
1. Create an empty dictionary to store the result
2. Recursively process each dictionary
3. When we reach the last level, we can add a key-value pair to the result, removing any empty keys
'''
def flatten_dictionary(dictionary: DeepNestedDict) -> Dict[str, str]:
    result = {}

    def traverse(dictionary, buffer):
        for key, value in dictionary.items():
            buffer.append(key)

            if type(value) == dict:
                traverse(value, buffer)
                if buffer:
                    buffer.pop()
            else:
                new_key = '.'.join(x for x in buffer if x)  # Remove empty keys
                result[new_key] = value
            
                if buffer:
                    buffer.pop()
            
    traverse(dictionary, [])
    return result

  
# debug your code below
dict_input = {
    "Key1": "1",
    "Key2": {
        "a": "2",
        "b": "3",
        "c": {
            "d": "3",
            "e": {
                "l": 20,
                "": "1",
                "z": 10
            }
        },
        "f":"7",
        "": {
            "z": '123'
        }
    },
    "Key3": "5"
}

print(flatten_dictionary(dict_input))
