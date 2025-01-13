'''
https://www.tryexponent.com/courses/swe-practice/basic-regex-parser

This solution assumes .* is not valid.

TC: O(T)
SC: O(1)
'''
def is_match(text: str, pattern: str) -> bool:
    t = p = 0
    T, P = len(text), len(pattern)
    while t < T and p < P:
        # Asterisk wildcard
        if pattern[p].isalpha() and p + 1 < P and pattern[p+1] == '*':
            while t < T and text[t] == pattern[p]:
                t += 1
            t -= 1
            p += 1
            
        # Fixed character
        elif pattern[p].isalpha() and text[t] != pattern[p]:
            return False

        # Dot character doesn't need an if statement as it automatically gets matched

        t += 1
        p += 1

    # Check for extra * wildcards in pattern
    while p < P and pattern[p].isalpha() and p + 1 < P and pattern[p+1] == '*':
        p += 2

    return t == T and p == P
  
