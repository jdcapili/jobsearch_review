# Arrays
- Simplest data structure.
- Contiguous block of memory, used to represent sequences.

## Tips
- Array problems often have simple brute.force solutions that use O(n) space, but there are subtler
solutions that use the array itself to reduce space complexity to O(1).
- Filling an array from the front is slow, so see if it's possible to write values from the back
- Instead of deleting an entry (which requires moving all entries to its left), consider overwriting
it.
- When dealing with integers encoded by an array consider processing the digits from the back
of the array. Altemately, reverse the array so the least-significant digit is the first entry.
- Be comfortable with writing code that operates on subarrays
- It's incredibly easy to make off-by-l errors when operating on arrays-reading past the last
element of an array is a comrnon error which has catastrophic consequences.
- Don't worry about preserving the integrity of the array (sortedness, keeping equal entries
together, etc.) until it is time to retum.
