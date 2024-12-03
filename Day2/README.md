## Time spent

~20-25 minutes

## Thoughts

This one was a bit more challenging than the previous, I was really overcomplicating it until I decided to separate the logic into the is_valid() helper function and focus on the base case of a list being valid or not.

### Part 1
#### Time spent: ~5 minutes
This one was relatively straight forward, just had to get the indexing down properly.
Got slightly tripped up on making sure it was increasing or decreasing from the beginning,
but just decided to manually compare the first 2 values.

### Part 2
#### Time spent: ~15-20 minutes
This part really tripped me up, I originally thought it would be easy to just add on
additional logic to what I had done in part 1 (which at the time wasn't separated into a helper function)
but that ended up being so messy and confusing trying to have like multiple different checks on a couple different booleans. Bad bad bad
So I then separated out the logic into "is this a valid list, yes or no?", and that made it so much easier.
I then just checked validity on base lists, if it was, good. If it wasn't, then I split it into a list of lists where each one was an iteration with 1 number removed, and checked if all of those were valid. If one was, boom. Ezpz