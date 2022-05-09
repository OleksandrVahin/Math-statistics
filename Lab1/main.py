import math
import matplotlib.pyplot as plt

sample = []
with open('data.txt') as data:
    for line in data:
        sample.extend(map(float, line.strip().split()))
print("Sample:\n", *sample)
sample.sort()
print("Sorted sample:\n", *sample)
k = 1 + int(3.322 * math.log(len(sample), 10))
print(k)
d = round((sample[-1] - sample[0])/k, 2)
print(d)
interval_series = {}
a = sample[0]
i = 0
for n in sample:
    if not a + i * d <= n < a + (i + 1) * d:
        i += 1
    interval_series[(a + i * d, a + (i + 1) * d)] = interval_series.get((a + i * d, a + (i + 1) * d), 0) + 1
plt.hist(sample, k)
plt.show()