import random


class Initilization:
    def __init__(self, fit_func, size, dimension=2):
        self.dimension = dimension
        self.fit_func = fit_func
        self.size = size
        if fit_func == 'rastrigin':
            self.min = -5.12
            self.max = 5.12
        if fit_func == 'sphere' or fit_func == 'rosenbrock':
            self.min = -10**4
            self.max = 10**4

    def random(self):
        population = []
        for i in range(self.size):
            chromo = [random.uniform(self.min, self.max)
                      for _ in range(self.dimension)]
            population.append(chromo)
        return population

    def grid(self):
        population = [[]]
        amount_per_dimension = int(self.size**(1/(self.dimension)))
        if amount_per_dimension ** self.dimension != self.size:
            print(
                f'Not a dimension root population size. Will instead use {amount_per_dimension*amount_per_dimension}')
        space = (self.max - self.min)/(amount_per_dimension - 1)

        for i in range(self.dimension):  # evenly distributes population.
            new_population = []
            for chromo in population:  # loops through each member of the population
                j = self.min
                while (j < (self.max + 0.1)):
                    # new chromosome generated each time each with the current values + the new dimension with a number from -5.12 -5.12
                    if (j > self.max):
                        j = self.max
                    new_chromo = chromo + [j]
                    new_population.append(new_chromo)
                    j += space
            population = new_population
        return population
