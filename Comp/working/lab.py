from Pyro4 import expose


class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers

    def solve(self):
        self.write_text("Count of workers: ")
        self.write_text(len(self.workers))
        self.write_text('\n')

        lines = self.read_input()
        workers_count = len(self.workers)
        md = (len(lines))
        worker_work = (len(lines))
        mapped = [None] * workers_count
        start = 0
        end = 0
        for worker_index in range(workers_count):
            end = start + worker_work
            if (md > 0):
                end += 1
                md -= 1
            mapped[worker_index] = self.workers[worker_index].mymap(lines[start:end], worker_index)
            start = end

        result = self.myreduce(mapped)
        self.write_output(result)
        self.write_text("Job finished.")

    def read_input(self):
        file = open(self.input_file_name, 'r')
        lines = [line.rstrip('\n') for line in file]
        file.close()
        return lines

    def write_text(self, result):
        file = open(self.output_file_name, 'a')
        file.write(str(result))
        file.close()

    def write_output(self, result):
        file = open(self.output_file_name, 'a')
        for element in result:
            file.write(str(element))
            file.write("\n")
        file.close()

    @staticmethod
    @expose
    def mymap(lines, ind):
        def josephus_problem(n, k):
            i = 1
            res = 0
            while i < n:
                i += 1
                res = (res + k) % i
            return res + 1

        result = []
        for line in lines:
            a1, b1 = map(str, line.split())
            a = int(a1)
            b = int(b1)
            r = str(ind) + " Having " + str(a) + " people and kill each " + str(
                b) + ". Surviver's place is # " + str(josephus_problem(a, b))
            result.append(r)
        return result

    @staticmethod
    @expose
    def myreduce(mapped):
        output = []
        for x in mapped:
            output.extend(x.value)
        return output

if __name__ == '__main__':
     master = Solver([Solver(), Solver()],
            "/Users/alexandrtotskiy/Developer/Distributed-processing-systems/Comp/working/input.txt",
            "/Users/alexandrtotskiy/Developer/Distributed-processing-systems/Comp/working/output.txt")
     master.solve()