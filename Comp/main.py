import random

from Pyro4 import expose

def point_in_polygon(polygon, point):
    """
    Raycasting Algorithm to find out whether a point is in a given polygon.
    Performs the even-odd-rule Algorithm to find out whether a point is in a given polygon.
    This runs in O(n) where n is the number of edges of the polygon.
     *
    :param polygon: an array representation of the polygon where polygon[i][0] is the x Value of the i-th point and polygon[i][1] is the y Value.
    :param point:   an array representation of the point where point[0] is its x Value and point[1] is its y Value
    :return: whether the point is in the polygon (not on the edge, just turn < into <= and > into >= for that)
    """

    # A point is in a polygon if a line from the point to infinity crosses the polygon an odd number of times
    odd = False
    # For each edge (In this case for each point of the polygon and the previous one)
    i = 0
    j = len(polygon) - 1
    while i < len(polygon) - 1:
        i = i + 1
        # If a line from the point into infinity crosses this edge
        # One point needs to be above, one below our y coordinate
        # ...and the edge doesn't cross our Y corrdinate before our x coordinate (but between our x coordinate and infinity)

        if (((polygon[i][1] > point[1]) != (polygon[j][1] > point[1])) and (point[0] < (
                (polygon[j][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / (polygon[j][1] - polygon[i][1])) +
                                                                            polygon[i][0])):
            # Invert odd
            odd = not odd
        j = i
    # If the number of crossings was odd, the point is in the polygon
    return odd

class Solver:
    def __init__(self, workers = None, input_file_name = None, output_file_name = None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers

    def solve(self):
        n = self.read_input()
        number_of_points = int(n / len(self.workers))
        # self.write_output("Count of workers: ")
        # self.write_output(len(self.workers))
        # self.write_output('\n')
        worker_amount = len(self.workers)

        mapped = [None] * worker_amount

        for i in range(0, worker_amount):
            mapped[i] = self.workers[i].mymap(i*number_of_points, i*number_of_points + number_of_points)

        result = self.myreduce(mapped)
        self.write_output(result)
        # self.write_output("Job finished!")

    @staticmethod
    @expose
    def mymap(a, b):
        polygon = [(0, 0), (200, 0), (100, 100), (0, 100)]
        n = 4
        points = []
        for _ in range(a, b):
            point = (random.randint(0, 300), random.randint(0, 300))
            points.append(point)

        result = []
        for i in range(len(points)):
            # if Solver.checkInside(polygon, n, points[i]):
            if point_in_polygon(polygon, points[i]):
                is_inside = " is inside of polygon"
            else:
                is_inside = " is outside of polygon"
            res = points[i].__str__() + is_inside + '\n'
            result.append(res)
        return result

    @staticmethod
    @expose
    def myreduce(mapped):
        output = []
        for x in mapped:
            output.extend(x.value)
        return output

    def read_input(self):
        f = open(self.input_file_name, 'r')
        line = f.readline()
        f.close()
        return int(line)

    def write_output(self, output):
        file = open(self.output_file_name, 'w')
        for element in output:
            file.write(str(element))
            # file.write("\n")
        file.close()
        # f = open(self.output_file_name, 'a')
        # f.write(str(output) + '\n')
        # f.close()

if __name__ == '__main__':
     master = Solver([Solver(), Solver()],
                     "/Users/alexandrtotskiy/Developer/Distributed-processing-systems/Comp/input.txt",
                     "/Users/alexandrtotskiy/Developer/Distributed-processing-systems/Comp/output.txt")
     master.solve()