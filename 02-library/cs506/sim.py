def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    return sum([ abs(x[i] - y[i]) for i in range(len(x)) ])

def jaccard_dist(x, y):
    # We assume x and y are binary vectors
    sanity_check(x, y)
    union = sum([1 for i in range(len(x)) if (x[i] == 1 or y[i] == 1)])
    intersection = sum([1 for i in range(len(x)) if (x[i] == 1 and y[i] == 1)])
    print(union, intersection)
    return 1 - (intersection / union)

def cosine_sim(x, y):
    sanity_check(x, y)
    dot_product = sum([x[i] * y[i] for i in range(len(x))])
    x_mag = (sum([xi**2 for xi in x]))**(1/2)
    y_mag = (sum([yi**2 for yi in y]))**(1/2)
    print(dot_product, x_mag, y_mag)
    return dot_product / (x_mag * y_mag)

def sanity_check(x,y):
    if (len(x) == 0 or len(y) == 0):
        raise ValueError("lengths must not be zero")
    if (len(x) != len(y)):
        raise ValueError("lengths must be equal")

# Feel free to add more
