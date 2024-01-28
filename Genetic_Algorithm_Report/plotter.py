import statistics
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from selection import Selection


class Plotter:
    def __init__(self, fit_func):
        self.max = []
        self.min = []
        self.avg = []
        self.std_dev = []
        self.fit_func = fit_func

    def compute_stats(self, population):
        fitness_array = [self.fit_func(x) for x in population]
        self.min.append(min(fitness_array))
        self.max.append(max(fitness_array))
        self.avg.append(sum(fitness_array) / len(fitness_array))
        self.std_dev.append(statistics.stdev(fitness_array))

    def plot_2D_population(self, population, fit_func, num):
        fig, ax = plt.subplots()
        min = -5.12 if num == 1 else -10**4
        max = 5.12 if num == 1 else 10**4
        x = np.linspace(min, max, 100)
        y = np.linspace(min, max, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.empty((100, 100))
        for i in range(100):
            for j in range(100):
                X[i, j], Y[j, j]
                Z[i, j] = fit_func([X[i, j], Y[i, j]])

        ax.set_title('Population vs Fitness Function')
        plt.contourf(X, Y, Z, levels=100, cmap='viridis')
        plt.colorbar()

        sc = ax.scatter([x[0] for x in population], [
            x[1] for x in population], color='white')
        plt.show()

    def make_plot(self, iterations):
        x = range(iterations)
        fig, ax = plt.subplots()
        ax.plot(x, self.avg, label='Average', color='blue')

        ax.plot(x, self.min, label='Minimum', color='green', linestyle='--')

        ax.plot(x, self.max, label='Maximum', color='red', linestyle='--')

        ax.set_title('Average, Minimum, and Maximum Values')
        ax.legend()
        plt.show()


class AnimatedScatter:

    def __init__(self, population_history, fit_func, num):
        self.populations = population_history
        self.fig, self.ax = plt.subplots()

        min = -5.12 if num == 1 else -10**4
        max = 5.12 if num == 1 else 10**4
        x = np.linspace(min, max, 100)
        y = np.linspace(min, max, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.empty((100, 100))
        for i in range(100):
            for j in range(100):
                X[i, j], Y[j, j]
                Z[i, j] = fit_func([X[i, j], Y[i, j]])

        plt.contourf(X, Y, Z, levels=100, cmap='viridis')
        plt.colorbar()
        self.sc = self.ax.scatter([x[0] for x in population_history[0]], [
            x[1] for x in population_history[0]], color='white')
        self.i = 1
        self.anim = None
        self.ax.set_title('Population vs Fitness Function')

    def update(self, frame):
        if self.i < len(self.populations):
            self.sc.set_offsets(self.populations[self.i])
            self.i += 1
        return self.sc,

    def start_animation(self):
        self.anim = FuncAnimation(
            self.fig, self.update, frames=len(self.populations), interval=300)
        plt.show()
