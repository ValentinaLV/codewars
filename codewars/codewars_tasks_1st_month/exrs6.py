"""
Socialist distribution
"""


def socialist_distribution(population, minimum):
    """
    You will be given two parameters, population and minimum: your goal is to give 
    to each one according to his own needs (which we assume to be equal to minimum 
    for everyone, no matter what), taking from the richest (bigger numbers) first.
    :param population: List[int]
    :param minimum: int
    :return: List[int]
    """""
    if len(population) * minimum > sum(population):
        return []

    while min(population) < minimum:
        i_max = population.index(max(population))
        i_min = population.index(min(population))
        population[i_max] -= 1
        population[i_min] += 1

    return population


def sum_cubes(n):
    return sum([num ** 3 for num in range(1, n + 1)])


print((sum_cubes(4)))

print([num for num in range(1, 5)])
