import matplotlib.pyplot as plt
import numpy as np


class Line:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.x1, self.y1 = point1.get_x(), point1.get_y()
        self.x2, self.y2 = point2.get_x(), point2.get_y()
        self.slope = (self.y1 - self.y2) / (self.x1 - self.x2)
        self.y_int = self.y1 / (self.slope * self.x1)

    def plot(self):
        plt.plot([self.x1, self.x2], [self.y1, self.y2])

    @property
    def points(self):
        return np.array([self.point1, self.point2])


class ConvexPolygon:

    def __init__(self, *lines):
        self.lines = lines
        self.x = True
        self.vertices = np.unique([np.array(point) for line in self.lines for point in line.points], axis=0)

    def plot(self):
        for line in self.lines:
            line.plot(color='r')

    @property
    def number_sides(self):
        return len(self.lines)


def sort_points(data):
    if len(data) < 2:
        return

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    sort_points(left)
    sort_points(right)

    i = j = k = 0

    while i < len(left) and j < len(right) and k < len(data):
        if left[i][1] == right[j][1]:
            if left[i][0] < right[j][0]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
        elif left[i][1] < right[j][1]:
            data[k] = left[i]
            i += 1
        else:
            data[k] = right[i]
            j += 1
        k += 1

    if i < len(left):
        data[k] = left[i]
        i += 1
        k += 1

    if j < len(right):
        j += 1
        k += 1

    return data


def generate_points(n):
    data = np.random.randn(n * 2).reshape(n, 2)  # Generate 250 random co-ordinates

    return data


def convex_hull():
    points = generate_points(250)

    if plt:
        plt.scatter(points.T[0], points.T[1], s=10)  # Display all the points

    points = sort_points(points)
    print(points)

    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    convex_hull()


