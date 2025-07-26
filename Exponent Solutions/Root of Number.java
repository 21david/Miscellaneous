import java.io.*;
import java.util.*;

/*  
Binary search on the possible answer space to find the
answer in O(logX) time. 
SC = O(1)
*/
class Solution {
  static double root(double x, int n) {
    if (n == 1)
        return x;

    double lo = 0, hi = x;
    double mid = 1.0;
    double power;
    while (hi - lo >= 0.001) {
        mid = (lo + hi) / 2;

        power = Math.pow(mid, n);
        if (power > x)
            hi = mid;
        else if (power < x)
            lo = mid;
        else
            return mid;  
    }

    return mid;
  }

  public static void main(String[] args) {
    System.out.println(root(7, 3));
  }
}

/*
From interviewer:
Thus, since lowerBound< root < upperBound, 
then the true error - |root-approxRoot|, 
satisfies |root-approxRoot| < (approxRoot - lowerBound) - 
so it is indeed enough to check when the value on the right side is lower than 0.001.
 2 4 0 and 0 is less than 0.001 2
 7 3 1.99999
 upper 1.999
 midPoint 1.998
 lower 1.997
 midpoint-lowerbound 1.999-1.998 <=0.001
*/
  
/*  
x = 7, n = 3
lo = 1.75
hi = 3.5
mid = 2.67
power = 5.3
*/
