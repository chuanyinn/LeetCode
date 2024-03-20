1. dp technique. Initialize an array of size `amount + 1` consisting of all zeros. The dp step is a sum of two previous dp's.
2. Careful about initialization, specifying zero on a finite sized dictionary is better than leaving it open-ended as defaultdict (might run into runtime error issues as the size of the dictionary changes in a loop). Also careful about handling of cases where coins of the same denomination are being considered multiple times.