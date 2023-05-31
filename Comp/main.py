import random

from Pyro4 import expose

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'[x: {self.x}, y: {self.y}]'

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

def onLine(l1, p):
    if (
        p.x <= max(l1.p1.x, l1.p2.x)
        and p.x <= min(l1.p1.x, l1.p2.x)
        and (p.y <= max(l1.p1.y, l1.p2.y) and p.y <= min(l1.p1.y, l1.p2.y))
    ):
        return True
    return False

def direction(a, b, c):
    val = (b.y - a.y) * (c.x - b.x) - (b.x - a.x) * (c.y - b.y)
    if val == 0:
        return 0
    elif val < 0:
        return 2
    return 1

def isIntersect(l1, l2):
    dir1 = direction(l1.p1, l1.p2, l2.p1)
    dir2 = direction(l1.p1, l1.p2, l2.p2)
    dir3 = direction(l2.p1, l2.p2, l1.p1)
    dir4 = direction(l2.p1, l2.p2, l1.p2)

    if dir1 != dir2 and dir3 != dir4:
        return True

    if dir1 == 0 and onLine(l1, l2.p1):
        return True

    if dir2 == 0 and onLine(l1, l2.p2):
        return True

    if dir3 == 0 and onLine(l2, l1.p1):
        return True

    if dir4 == 0 and onLine(l2, l1.p2):
        return True

    return False


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

        mapped = []

        mapped = [None] * worker_amount

        for i in range(0, worker_amount):
            mapped[i] = self.workers[i].mymap(i*number_of_points, i*number_of_points + number_of_points)

        result = self.myreduce(mapped)
        self.write_output(result)
        # self.write_output("Job finished!")

    @staticmethod
    @expose
    def mymap(a, b):
        polygon = [Point(0, 0), Point(200, 0), Point(100, 100), Point(0, 100)]
        n = 4
        points = []
        for _ in range(a, b):
            point = Point(random.randint(0, 400), random.randint(0, 400))
            points.append(point)

        result = []
        for i in range(len(points)):
            if Solver.checkInside(polygon, n, points[i]):
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

    @staticmethod
    @expose
    def checkInside(poly, n, p):
        if n < 3:
            return False

        exline = Line(p, Point(9999, p.y))
        count = 0
        i = 0
        while True:
            side = Line(poly[i], poly[(i + 1) % n])
            if isIntersect(side, exline):
                if direction(side.p1, p, side.p2) == 0:
                    return onLine(side, p)
                count += 1

            i = (i + 1) % n
            if i == 0:
                break

        return count & 1

    def read_input(self):
        f = open(self.input_file_name, 'r')
        line = f.readline()
        f.close()
        return int(line)

    def write_output(self, output):
        file = open(self.output_file_name, 'w')
        for element in output:
            file.write(str(element))
            file.write("\n")
        file.close()
        # f = open(self.output_file_name, 'a')
        # f.write(str(output) + '\n')
        # f.close()

if __name__ == '__main__':
     master = Solver([Solver(), Solver()],
     "/Users/alexandrtotskiy/Developer/Comp/input.txt",
                     "/working/output.txt")
     master.solve()