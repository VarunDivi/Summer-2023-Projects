import matplotlib.pyplot as plt
import numpy
import random

class Random_walk():

    def __init__(self, num_points = 5000):
        self.num_points = num_points

        self.x_val = [0]
        self.y_val = [0]

    def choose(self, l):
        return random.sample(l,1)[0]

    def walkPoints(self):
        i = 0

        while len(self.x_val) < self.num_points:
            x_dir = self.choose([-1,1])
            x_amnt = self.choose([1,2,3,4,5])
            x_move = x_dir * x_amnt

            y_dir = self.choose([-1,1])
            y_amnt = self.choose([1,2,3,4,5])
            y_move = y_dir * y_amnt

            next_x = self.x_val[-1] + x_move
            next_y = self.y_val[-1] + y_move

            self.x_val.append(next_x)
            self.y_val.append(next_y)

    def walkUntil(self, xTarget, yTarget):
        i = 0

        while self.x_val[-1] < xTarget or self.y_val[-1] < yTarget:
            x_dir = self.choose([-1,1])
            x_amnt = self.choose([1,2,3,4,5])
            x_move = x_dir * x_amnt

            y_dir = self.choose([-1,1])
            y_amnt = self.choose([1,2,3,4,5,6,7,8,9,10])
            y_move = y_dir * y_amnt

            next_x = self.x_val[-1] + x_move
            next_y = self.y_val[-1] + y_move

            self.x_val.append(next_x)
            self.y_val.append(next_y)
        print("It took " + str(max(len(self.x_val), len(self.y_val))) + " steps to reach the goal")


walker = Random_walk(100000)

walker.walkPoints()

plt.scatter(walker.x_val, walker.y_val, c=walker.y_val, cmap = plt.cm.Blues,s =1, edgecolors='none')

plt.show()