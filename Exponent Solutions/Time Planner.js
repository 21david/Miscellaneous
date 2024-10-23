// Written on October 22, 2024 after seeing the solution
function meetingPlanner(slotsA, slotsB, dur) {
    // Two pointer approach
    let a = 0, b = 0;
    let A = slotsA.length, B = slotsB.length;
    let a_avail, b_avail;
    let start, end;

    while (a < A && b < B) {
        a_avail = slotsA[a];
        b_avail = slotsB[b];

        // get overlap
        start = Math.max(a_avail[0], b_avail[0]);
        end = Math.min(a_avail[1], b_avail[1]);

        if (start + dur <= end) 
            return [start, start + dur];  // found an answer

        // else, we need to move pointer to whichever one is behind forward 
        else if (a_avail[1] < b_avail[1])
            a++;
        else
            b++;
    }

    return [];
}
