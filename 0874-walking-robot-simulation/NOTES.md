Originially right answer but TLE:
1. ​Change list of list into set of tuples to reduce lookup time `set(map(tuple, obstacles))`
2. Smart trick of `dir_idx = (dir_idx - 1) % 4`. I was originally using dict of dir: dir.
