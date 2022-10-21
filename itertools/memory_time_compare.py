import time
import sys
#pip install -U memory_profiler
#python -m memory_profiler memory_time_compare
#mprof run  memory_time_compare.py
#mprof plot

class MyCounters:
    @profile
    def __init__(self):
        pass

    @profile
    def count(self, start=0, step=1):
        '''
        https://docs.python.org/3/library/itertools.html
        # count(10) --> 10 11 12 13 14 ...
        # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
        '''
        self.n = start
        while True:
            yield self.n
            self.n += step

    @profile
    def count_end(self, end, start=0, step=1):
        n = start
        while n <= end:
            yield n
            n += step

    def count_ntimes(self, ntimes, start=0, step=1):
        # count(10) --> 10 11 12 13 14 ...
        # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
        n = start
        for i in range(ntimes):
            yield n
            n += step

    def fib(self, end):
        a, b = 0, 1
        while a <= end:
            yield a
            a, b = b, a + b


class MyCounter1:
    def __init__(self, end, start = 0, step = 1):
        if end < start:
            _ = start
            start = end
            end = _
        self.end = end
        self.start = start  # just for info
        self.x = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x
        x += self.step
        if x > self.end:
            raise StopIteration
        self.x = x
        return x


if __name__ == "__main__":

    end = 10000000

    counter1 = MyCounter1(end)

    print('''counter1 = MyCounter1(end)\nnext(counter):''')
    print(next(counter1))
    print(next(counter1))
    input("I used iterator with {} bytes usage (Press enter to continue)".format(sys.getsizeof(counter1)))
    print()

    my_counter = MyCounters()

    print('my_counter = MyCounters()\ncounter = map("{:02}".format, my_counter.count(1))\nnext(counter):')
    counter = map("{:02}".format, my_counter.count(1))
    print(next(counter))
    print(next(counter))
    input("I used infinite generator with {} bytes usage (Press enter to continue)".format(sys.getsizeof(counter)))
    print()

    print('my_counter = MyCounters()\ncounter = map("{:02}".format, my_counter.count_end(end))\nnext(counter):')
    counter = map("{:02}".format, my_counter.count_end(end))
    print(next(counter))
    print(next(counter))
    input("I used large generator with {} bytes usage (Press enter to continue)".format(sys.getsizeof(counter)))
    print()

    print('my_counter = MyCounters()\nlist(map(lambda x: x, my_counter.count_end(end))):')
    counter = list(map(lambda x: x, my_counter.count_end(end)))
    #print(next(counter))
    #print(next(counter))
    input("I used large generator to list with {} bytes usage (Press enter to continue)".format(sys.getsizeof(counter)))
    print()

    del(counter)

    start = time.perf_counter()
    for i in range(end):
        pass
    end = time.perf_counter()
    input("I used range in for loop, it took {} seconds (Press enter to continue)".format(end-start))
    print()

    start = time.perf_counter()
    for i in counter1:
        pass
    end = time.perf_counter()
    input("I used iterator in for loop, it took {} seconds (Press enter to continue)".format(end-start))
    print()

    start = time.perf_counter()
    for i in map(lambda x: x, my_counter.count_end(end)):
        pass
    end = time.perf_counter()
    input("I used large generator, it took {} seconds (Press enter to continue)".format(end-start))
    print()

    start = time.perf_counter()
    for i in list(map(lambda x: x, my_counter.count_end(end))):
        pass
    end = time.perf_counter()
    input("I used large generator to list, it took {} seconds (Press enter to continue)".format(end-start))
    print()
