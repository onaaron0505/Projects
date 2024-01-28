import random
import numpy as np


class Mutation:
    def __init__(self, rate, fit_func, dimension=2):
        self.dimension = dimension
        self.rate = rate
        if fit_func == 'rastrigin':
            self.min = -5.12
            self.max = 5.12
        if fit_func == 'sphere' or fit_func == 'rosenbrock':
            self.min = -10**4
            self.max = 10**4

    def uniform_random(self, population, length):
        for i in range(len(population)):
            for x in range(len(population[i])):
                if random.random() < self.rate:
                    population[i][x] = min(
                        max(random.uniform(-length, length+0.000001) + x, self.min), self.max)
        return population

    def gaussian(self, population, sigma):
        for i in range(len(population)):
            for x in range(len(population[i])):
                if random.random() < self.rate:
                    population[i][x] = min(
                        max(np.random.normal(x, sigma), self.min), self.max)
        return population
