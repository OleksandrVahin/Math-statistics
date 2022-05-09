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


# Extracting initial data
realization = extract_data()
print("Realization:\n", *realization)

# Sorting sample
realization.sort()
print("Sorted realization:\n", *realization)

# Calculating some properties
k = sturges_rule(realization)
r = realization[-1] - realization[0]
d = r2(r / k)
print(f"Number of bins: {k}\n"
      f"Range of realization: {r}\n"
      f"Width of bin: {d}")
interval_series = {}
a = realization[0]
i = 0
for n in realization:
    if not a + i * d <= n < a + (i + 1) * d:
        i += 1
    interval_series[(a + i * d, a + (i + 1) * d)] = interval_series.get((a + i * d, a + (i + 1) * d), 0) + 1
plt.hist(realization, k)
plt.show()