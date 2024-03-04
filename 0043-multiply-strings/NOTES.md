1. when adding the product and carry to the respective indices, can't just specify result[i+j] and result[i+j+1] as there might be overflow due to previously added number. So should add the temporary (two-digit) product to [i+j] location, then take the reminder and overflow part of the whole thing. 
2. to get rid of leading zeros, at one point at the end of a list, can conveniently use pop() function while checking that it's zero, and length is long enough.
3. list to string, use ''.join() method.​
