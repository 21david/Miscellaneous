// https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&sortBy=submissions

class Solution {
    public static ArrayList<Integer> subarraySum(int[] arr, int n, int s) {
        // Sliding window
        int l = 0;
        int cur_sum = 0;
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int r = 0; r < arr.length; r++) {
            cur_sum += arr[r];
            
            while (cur_sum >= s && l <= r) {
                if (cur_sum == s) {
                    answer.add(l+1);
                    answer.add(r+1);
                    return answer;
                }
                cur_sum -= arr[l++];
            }
        }
        
        
        answer.add(-1);
        return answer;
    }
}

/*
Test cases:
(number of elements) (target sum)
(all the array elements)

5 12
1 2 3 7 5

1 0
0

4 0
1 2 3 4

5 0
1 4 5 6 0
=> 5 5

*/
