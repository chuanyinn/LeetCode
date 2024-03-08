1. DP technique: store each word as the key, and maximum chain ending at that word. Maximum chain happens at either starting new at that word, or adding one to a previous predecessor.
2. Looking for predecessors: sort the words list, and for each word to be processed, loop over the letters to subtract one letter to form a predecessor to search for.
