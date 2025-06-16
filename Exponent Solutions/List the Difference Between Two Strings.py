# https://www.tryexponent.com/courses/swe-practice/diff-between-two-strings

from typing import List

# Needs debugging, but close
def diff_between_two_strings(source: str, target: str) -> List[str]:
    S, T = len(source), len(target)  # S = num columns,  T = num rows
    
    # def lcs(s, t):
    #     if source[s] == target[t]:
    #         return 1 + lcs(s+1, t+1)
    #     else:
    #         lcs(s+1, t)
    #         lcs(s, t+1)

    # LCS matrix
    dp = [[0] * (S+1) for _ in range(T+1)]
    for t in range(T-1, -1, -1):  # rows
        for s in range(S-1, -1, -1):  # columns
            if target[t] == source[s]:
                dp[t][s] = dp[t+1][s+1] + 1
            else:
                dp[t][s] = max(dp[t+1][s], dp[t][s+1])

    # print(str(dp).replace('],', '],\n'))
    # Find answer
    s = t = 0
    ans = []
    while s < S and t < T:
        # print(s,t)
        while s+1 < S and dp[t][s+1] == dp[t][s]:
            # print(s)
            print(f'-{source[s]}')
            ans.append(f'-{source[s]}')
            s += 1
        while t+1 < T and dp[t+1][s] == dp[t][s]:
            print(f'+{target[t]}')
            ans.append(f'+{target[t]}')
            t += 1
        print(source[s])
        ans.append(source[s])
        s += 1
        t += 1

    while t < T:
        ans.append(f'+{target[t]}')
        t += 1

    print(ans)
    return ans


# debug your code below
print(diff_between_two_strings("ABCDEFG", "ABDFFGH"))
'''  
   A  B  C  D  E  F  G
A [5, 4, 3, 3, 2, 2, 1, 0],
B [4, 4, 3, 3, 2, 2, 1, 0],
D [3, 3, 3, 3, 2, 2, 1, 0],
F [2, 2, 2, 2, 2, 2, 1, 0],
F [2, 2, 2, 2, 2, 2, 1, 0],
G [1, 1, 1, 1, 1, 1, 1, 0],
H [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0]]

'''
'''  
AB C D E F   G
AB   D   F F G H


'''
