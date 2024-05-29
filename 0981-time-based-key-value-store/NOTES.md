`SortedDict`
- We use the `bisect_right` method from SortedDict to find the insertion point for the given timestamp. This method returns the index of the first element greater than the given timestamp.
- Otherwise, we use `peekitem` with `idx - 1` to get the item at the position just before the insertion point and return its value.
- This implementation makes efficient use of `SortedDict` for both storing and retrieving timestamped values, ensuring that the set and get operations are efficient, typically `O(log N)`, where `N` is the number of timestamps for a given key.
- Note that `bisect_right` only works for `SortedDict` and not `OrderedDict`.​
