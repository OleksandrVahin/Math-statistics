sample = []
with open('data.txt') as data:
    for line in data:
        sample.extend(map(float, line.strip().split()))
print(*sample)
