// https://structy.net/problems/non-adjacent-sum

import java.util.*;

class Source {
  private static int help(List<Integer> nums, int s, Map<Integer, Integer> memo) {
    // if taken or skipped all, return 0
    if (s >= nums.size()) return 0;

    // use DP memoization
    if (memo.containsKey(s)) return memo.get(s);

    // take curr num
    int op1 = nums.get(s) + help(nums, s+2, memo);

    // skip curr num
    int op2 = help(nums, s+1, memo);

    int max = Math.max(op1, op2);
    
    memo.put(s, max);  // memoize
    return max;
  }
  
  public static int nonAdjacentSum(List<Integer> nums) {
    Map<Integer, Integer> memo = new HashMap<>();
    int max = help(nums, 0, memo);
    return max;
  }

  public static void run() {
    // this function behaves as `main()` for the 'run' command
    // you may sandbox in this function , but should not remove it
  }
}
