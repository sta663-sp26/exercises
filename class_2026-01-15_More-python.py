## Exercise 1

# Using list comprehensions, complete the following tasks:

# * Create a list containing tuples of x and y coordinates of all points of a regular grid for 𝑥∈[0,10] and 𝑦∈[0,10]

g = [ (x,y) for x in range(0,11) for y in range(0,11) ]
g
len(g)

# * Count the number of points where 𝑦>𝑥

len( [ (x,y) for x,y in g if y > x ] )

# * Count the number of points where 𝑥 or 𝑦 is prime.

prime = (2,3,5,7)

len([ (x,y) for x,y in g if x in prime or y in prime ])



## Exercise 2
# Write a function, kg_to_lb, that converts a list of weights 
# in kilograms to a list of weights in pounds 
# (1 kg = 2.20462 lbs). 
# Include a doc string and function annotations.

def kg_to_lbs(wt: list[float]) -> list[float]:
    """Covert a list of weights in kg to lbs"""

    return [x*2.20462 for x in wt]


# Write a second function, total_lb, that calculates 
# the total weight in pounds of an order, the input 
# arguments should be a list of item weights in kilograms 
# and a list of the number of each item ordered.

def total_lb(wt: list[float], n: list[int]) -> float:
    "Calculate the total weight of each order in lbs"

    return sum([x*y*2.20462 for x,y in zip(wt, n)])
