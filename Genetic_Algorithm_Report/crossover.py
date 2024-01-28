import random
import copy
import numpy as np


class Crossover:
    def __init__(self, fit_func, dimension=2):
        self.dimension = dimension
        if fit_func == 'rastrigin':
            self.min = -5.12
            self.max = 5.12
        if fit_func == 'sphere' or fit_func == 'rosenbrock':
            self.min = -10**4
            self.max = 10**4

    def two_point(self, population, num_elites, distance=-1):
        children = []
        point1 = random.randint(0, self.dimension-1)
        if (distance == -1):
            point2 = random.randint(point1, self.dimension-1)
        else:
            point2 = point1+distance
        for i in range(len(population)-num_elites*2-1, -1, -2):
            if (i < 1):
                children.append(copy.deepcopy(population[0]))
                break
            chromo1 = population.pop(random.randint(0, i))
            chromo2 = population.pop(random.randint(0, i-1))
            temp = chromo2[:]
            chromo2[point1:point2+1] = chromo1[point1:point2+1]
            chromo1[point1:point2+1] = temp[point1:point2+1]
            children.append(chromo1)
        return children

    # https://dl.acm.org/doi/pdf/10.5555/2933923.2933986 link for help on SPX paper.
    def SPX(self, population, num_elites):
        children = []
        parents = copy.deepcopy(population)
        j = 0
        while len(children) < (len(parents)/2-num_elites):
            parent1 = population.pop(random.randint(0, len(population)-1))
            parent2 = population.pop(random.randint(0, len(population)-1))
            parent3 = population.pop(random.randint(0, len(population)-1))
            center = 1/3 * np.add(np.add(parent1, parent2), parent3)

            y = [(1+0.3)*np.subtract(parent1, center), (1+0.3) *
                 np.subtract(parent2, center), (1+0.3)*np.subtract(parent3, center)]
            length = 1 if j % 2 == 0 else 2
            for i in range(length):
                children.append(self.random_point_in_simplex(y, center))
            j += 1

        return children

    def random_point_in_simplex(self, vertices, center):
        weights = [random.random() for _ in range(len(center))]

        weights = [w / sum(weights) for w in weights]

        for i in range(len(vertices)):
            for j in range(len(center)):
                center[j] += weights[j] * vertices[i][j]
        return center
