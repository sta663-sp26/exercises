## Exercise 1

x = {"a": 1, "b": 2, "c": 3}
y = {"c": 5, "d": 6, "e": 7}

# Replicate the output from
print(x | y)


### Method 1

def merge(d1, d2):
    z = d1.copy()
    for k,v in d2.items():
        z[k] = v

    return(z)

print("m = ", merge(x,y), "\nx = ", x, "\ny = ", y)


### Method 2

def merge(d1, d2):
    z = d1.copy()
    z.update(d2)

    return(z)

print("m = ", merge(x,y), "\nx = ", x, "\ny = ", y)

### Method 3

def merge(d1, d2):
    return( {**d1, **d2} )

print("m = ", merge(x,y), "\nx = ", x, "\ny = ", y)


## Exercise 2

# A fixed collection of 100 integers.
# - vector / array

# A queue (first in first out) of customer records.
# - deque 

# A stack (first in last out) of customer records.
# - vector / array / list

# A count of word occurrences within a document.
# - dictionary / hashmap

# The heights of the bars in a histogram with even binwidths.
# - vector / array / list