# includes
from initilization import Initilization
from crossover import Crossover
from selection import Selection
from mutation import Mutation
from plotter import Plotter, AnimatedScatter
import copy
import time


def sort_func(element):
    return element[1]


functions = ['sphere', 'rastrigin', 'rosenbrock']

# setup
for j in range(3):
    iterations = 100
    dim = 2
    fit_func = functions[j]
    num_elites = 5
    init = Initilization(fit_func, 144, dim)
    cross = Crossover(fit_func, dim)
    selc = Selection(fit_func, dim)
    mut = Mutation(0.03, fit_func, dim)
    plt = Plotter(selc.fit_func)

    # initilization
    start = time.time()

    population_histories = []

    population = init.random()  # random initilization
    # population = init.grid() #grid initilization

    plt.compute_stats(population)

    population_histories.append(population)
    i = 0
    # while plt.min[i] > 0.09: # fitness termination
    while i < iterations:  # fixed termination

        # eval fitness
        fitness_array = [[x, selc.fit_func(x)] for x in population]

        # selection
        elites = sorted(fitness_array, key=sort_func)
        elites = [copy.deepcopy(elite[0]) for elite in elites[0:num_elites]]
        population = selc.tournament(fitness_array)  # tournament selection
        # population = selc.rws(fitness_array) #rws

        # crossover

        population = cross.two_point(
            population, num_elites)  # two point cross over
        # population = cross.SPX(population, num_elites) #SPX crossover

        # mutation
        # population = mut.gaussian(copy.deepcopy(population), 0.6) #gaussian mutation
        population = mut.uniform_random(copy.deepcopy(
            population), 1)  # uniform random mutation
        population = elites + population

        i += 1

        # get data for reporting
        plt.compute_stats(population)
        population_histories.append(population)

    end = time.time()

    # perform reporting
    print(
        f'\n\n{j} - Population Statistics\n\taverage: {plt.avg[i]}\n\tstandard deviation: {plt.std_dev[i]}\n\tmin: {plt.min[i]}\n\tmax: {plt.max[i]}\n\ttime: {end-start}\n\titerations:{i}')

    animation = AnimatedScatter(population_histories, selc.fit_func, j)
    animation.start_animation()
    plt.make_plot(i+1)
