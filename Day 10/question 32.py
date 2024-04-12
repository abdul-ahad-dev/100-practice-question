import itertools

numbers = [1, 2, 3, 4, 5, 6]

combinations = itertools.combinations(numbers, 2)

for combination in combinations:
    print(combination)
