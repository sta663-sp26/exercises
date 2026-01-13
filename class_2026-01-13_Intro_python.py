## Exercise 1

d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Select only the odd values in this list

d[1::2]

# Select every 3rd value starting from the 2nd element.

d[1::3]

# Select every other value, in reverse order, starting from the 9th element.

d[8::-2]

# Select the 3rd element, the 5th element, and the 10th element

[d[2]] + [d[4]] + [d[9]]
[d[2], d[4], d[9]]


## Exercise 2

s = "the quick  Brown   fox Jumped  over   a Lazy  dog"

( s.replace("  ", " ")
   .replace("  ", " ")
   .lower()
   .replace("dog", "dog.")
   .capitalize()
)
