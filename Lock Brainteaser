// April 3, 2020
// David Espinosa

/*
Brainteaser:
      _
    /   \
   |     |
 __|_____|__
|           |
| [?][?][?] |
|           |
|____/ \____|

Can you open the lock using these clues?

682 -- One digit is right and in its place
614 -- One digit is right but in the wrong place
206 -- two digits are right but both are in the wrong place
738 -- all digits are wrong
380 -- one digit is right but in the wrong place

See graphic below:
imgur.com/a/WoQZWhS

*/

/*
After solving the problem above, I challenged myself to write an algorithm that would solve it. 
To my surprise, the algorithm produced the same number that was my answer to the brain teaser!

If there are other numbers that could create the same problem, those numbers could be replaced 
in the 'test' variables, and the algorithm should still be able to solve it.

I think this algorithm could be expanded to find different sets of numbers that also work for this 
kind of brain teaser. However, upon thinking about this more, it would have a search space of 10^15,
as there are 15 individual digits in the given numbers, and each one would have to iterate 
through 0 - 9. So probably only a very powerful computer could do this.
*/


class Main {

    static final int[] test1 = {6, 8, 2}; // one digit is right, and is in its place
    static final int[] test2 = {6, 1, 4}; // one digit is right, but is in the wrong place
    static final int[] test3 = {2, 0, 6}; // two digits are right, both are in the wrong place
    static final int[] test4 = {7, 3, 8}; // all digits are wrong
    static final int[] test5 = {3, 8, 0}; // one digit is right, but is in the wrong place


    public static void main(String[] args) {
        
        int[] temp;

        // try every combination from 000 to 999
        for(int n1 = 0; n1 <= 9; n1++)
            for(int n2 = 0; n2 <= 9; n2++)
                for(int n3 = 0; n3 <= 9; n3++)
                {
                    temp = new int[] {n1, n2, n3};

                    // if it follows the logic for all 5 given numbers, then it is a valid lock number
                    if( test1(temp)
                     && test2(temp)
                     && test3(temp)
                     && test4(temp)
                     && test5(temp) )
                    {
                        System.out.println("" + temp[0] + temp[1] + temp[2] + " is a valid lock number.");
                    }
                }
    }

    // return TRUE only if one digit from 'temp' matches the digit in the same position in 'test1'
    public static boolean test1(int[] temp)
    {
        boolean matched = false;

        for(int i = 0; i < temp.length; i++)
        {
            if(temp[i] == test1[i])
            {
                if(matched) // if more than one match, return false
                    return false;
                else
                    matched = true;
            }
        }

        return matched;
    }

    // return TRUE if only ONE digit is right, AND its in the WRONG place
    public static boolean test2(int[] temp)
    {
        // find how many match. if > 1 or < 1, return false
        // if only 1 matches, make sure their indices do not match

        int matched = 0;
        int matchedNum = 0;

        for(int i = 0; i < temp.length; i++)
        {
            for(int j = 0; j < test2.length; j++)
            {
                if(test2[j] == temp[i])
                {
                    matched++;
                    matchedNum = test2[j];
                }
            }
        }

        if (matched != 1)
            return false;
        
        // now that we know there was only 1 matched, make sure their indices do not match in the arrays
        for(int i = 0; i < temp.length; i++)
        {
            if(temp[i] == matchedNum)
            {
                if(temp[i] == test2[i]) // if their indices match, return false
                    return false;
            }
        }

        return true;
    }

    
    // returns true if and only if:
    //    two digits match
    //    both of those digits are not in the same place in both arrays (both have to be offset)
    public static boolean test3(int[] temp)
    {
        int matched = 0;
        int matchedNum1 = -1;
        int matchedNum2 = -1;

        for(int i = 0; i < temp.length; i++)
        {
            for(int j = 0; j < test3.length; j++)
            {
                if(test3[j] == temp[i])
                {
                    matched++;

                    if(matchedNum1 != -1)
                    {
                        matchedNum2 = test3[j];
                    }
                    else
                    {
                        matchedNum1 = test3[j];
                    }
                }
            }
        }

        if(matched != 2)
            return false;

        // now that we know there were only 2 matched, make sure their indices do not match in the arrays
        for(int i = 0; i < temp.length; i++)
        {
            if( (temp[i] == matchedNum1 && test3[i] == matchedNum1) || (temp[i] == matchedNum2 && test3[i] == matchedNum2) )
            {
                return false;
            }
        }

        return true;
    }

    // return FALSE if any element in temp is found in 'test3' array
    public static boolean test4(int[] temp)
    {
        for(int i = 0; i < temp.length; i++)
        {
            for(int j = 0; j < test4.length; j++)
            {
                if(temp[i] == test4[j])
                {
                    return false;
                }
            }
        }

        return true;
    }

    // return TRUE if only ONE digit is right, AND its in the WRONG place
    // (same as the test2() method)
    public static boolean test5(int[] temp)
    {
        // find how many match. if > 1 or < 1, return false
        // if only 1 matches, make sure their indices do not match

        int matched = 0;
        int matchedNum = 0;

        for(int i = 0; i < temp.length; i++)
        {
            for(int j = 0; j < test5.length; j++)
            {
                if(test5[j] == temp[i])
                {
                    matched++;
                    matchedNum = test5[j];
                }
            }
        }

        if (matched != 1)
            return false;
        
        // now that we know there was only 1 matched, make sure their indices do not match in the arrays
        for(int i = 0; i < temp.length; i++)
        {
            if(temp[i] == matchedNum)
            {
                if(temp[i] == test5[i]) // if their indices match, return false
                    return false;
            }
        }

        return true;
    }
}
