## Thoughts

Part 2 of this question has hands

## Total time spent: 4-5 hrs? maybe more I kinda stewed on it for days

### Part 1
#### Time spent: 20-30 min
This part was reletively simple, parsing was tedious and figuring out the exact logic on if a list is valid took a moment.
Decided to extract the parsing and checking validity of a single list to functions to make the code cleaner. Also helped
to simplify part 2 with that logic extracted.


### Part 2
#### Time spent: the rest
At first I tried generating permutations and seeing if it was valid, but it literally crashed my computer. On the plus side now
I remember that the number of permutations of a list is exponentional!
I then after discussing it with a friend came up with building the list bottom up, finding any value in the wrong spot and then
putting it in the first spot that would make the list invalid if it were to be any further.
This worked, then I got stuck on duplicating values for a while because I wasn't breaking and the rules were being checked multiple times.
This was very hard for me to figure out.
