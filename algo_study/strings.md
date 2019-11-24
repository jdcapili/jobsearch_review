# Key Operators
- s[i] -> indexing
- len(s) -> length
- s + t -> combining strings
- s[i:j] -> slicing.  has many variants
- s in t -> checking substring
- s.strip()
- s.startswith(prefix)
- s.endswith(suffix)
- s.split(',')
- 3 * s -> string multiplier
- ','.join((s1,s2,s3))
- s.tolower()
- 'Name {name}, Rank {rank}'.format(name='Archimedes', rank=3)

# Notes:
Understand the implications of a string type which is immutable, e.g., the need to allocate a
new string when concatenating immutable strings. Know alternatives to immutable strings,
e.g., a list in Python.