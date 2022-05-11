import math
import matplotlib.pyplot as plt
from functools import partial


def extract_data():
    """Returns list of floats from data.txt"""
    result = []
    with open('data.txt') as data:
        for line in data:
            result.extend(map(float, line.strip().split()))
    return result


def sturges_rule(sample):
    """Takes sample, returns number of bins that will be in histogram"""
    return 1 + int(math.log(len(sample), 2))


r2 = partial(round, ndigits=2)


def get_frequency(sample):
    """Takes sample, returns frequencies of intervals"""
    frequency = {}
    a = min(sample)
    i = 0
    for n in realization:
        if not a + i * d <= n < a + (i + 1) * d:
            i += 1
        frequency[i] = frequency.get(i, 0) + 1
    return frequency


# Extracting initial data
realization = extract_data()
print("Realization:\n", *realization)
print("Number of unique values:", len(set(realization)))

# Sorting sample
realization.sort()
print("Sorted realization:\n", *realization)

# Calculating some properties
k = sturges_rule(realization)
# 7 is too small, because histograms aren't beautiful let's take 8
k = 8
r = realization[-1] - realization[0]
d = r2(r / k)
print(f"Number of bins: {k}\n"
      f"Range of realization: {r}\n"
      f"Width of bin: {d}")

# Calculating frequencies for intervals
frequency = get_frequency(realization)
a = min(realization)
print("Frequencies:")
for x in map(lambda x: print(f'[{r2(a + x[0] * d)};{r2(a + (x[0] + 1) * d)}): {x[1]}'), frequency.items()):
    pass

# Drawing histogram of sample
plt.hist(realization, k)
plt.show()
