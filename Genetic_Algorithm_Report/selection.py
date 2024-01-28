import math
import random
import copy


class Selection:
    def __init__(self, fit_func, dimension=2):
        self.dimension = dimension
        if fit_func == 'rastrigin':
            self.fit_func = self.rastrigin
        if fit_func == 'sphere':
            self.fit_func = self.sphere
        if fit_func == 'rosenbrock':
            self.fit_func = self.rosenbrock

    def rws(self, population):
        parents = []
        size = len(population)
        total = 0
        for chromo in population:
            if (chromo[1] > 0.1 * 10**(-9)):
                total += 1/chromo[1]
            else:
                total += 1/(chromo[1] + 0.1 * 10**(-9))

        while (len(parents) < size*2):
            rand = random.random()
            sum = 0
            i = 0
            while (sum < rand):
                i += 1
                value = population[i-1][1] if population[i -
                                                         1][1] > 0.1 * 10**(-9) else 0.1 * 10**(-9)
                sum += (1/value)/total
            parents.append(copy.deepcopy(population[i-1][0]))
        return parents

    def tournament(self, population):
        parents = []
        size = len(population)
        while (len(parents) < (size*2)):
            i = 0
            index = random.randint(0, len(population) - 1)
            winner = population[index]

            while (i < 4):
                index = random.randint(0, len(population) - 1)
                if (winner[1] > population[index][1]):
                    winner = population[index]
                i += 1
            parents.append(copy.deepcopy(winner[0]))
        return parents

    def rastrigin(self, chromo):
        sum = 0
        A = 10
        for i in range(len(chromo)):
            sum += chromo[i] ** 2 - A * math.cos(2*math.pi*chromo[i])
        return A * len(chromo) + sum

    def sphere(self, chromo):
        sum = 0
        for i in range(len(chromo)):
            sum += chromo[i]**2
        return sum

    def rosenbrock(self, chromo):
        sum = 0
        for i in range(len(chromo)-1):
            sum = 100 * (chromo[i+1] - chromo[i]**2)**2 + (1 - chromo[i])**2
        return sum
