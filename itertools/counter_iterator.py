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



    def count(self, start=0, step=1):
        '''
        https://docs.python.org/3/library/itertools.html
        '''
        # count(10) --> 10 11 12 13 14 ...
        # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
        self.n = start
        while True:
            yield self.n
            self.n += step

    def count_end(self, end, start=0, step=1):
        # count(10) --> 10 11 12 13 14 ...
        # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
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


if __name__ == "__main__":

    print('''import itertools\ncounter = map("{:02}".format, itertools.count(1))\nnext(counter):''')

    import itertools
    #itertools.count(start=0, step=1)
    counter = map("{:02}".format, itertools.count(1))
    print(next(counter))
    print(next(counter))

    print()

    end = 10

    counter1 = MyCounter1(end)

    print('''counter1 = MyCounter1(end)\nnext(counter):''')

    print(next(counter1))
    print(next(counter1))

    for i in counter1:
        print(i)

    quit()

    print("Count start = 50, step = 5, break for loop at n > 100:")

    for n in my_counter.count(50,5):
        if n > end: break
        print(n, end = ' ')

    print("\n")

    print("Count start = 50, step = 5, while loop n <= 100:")

    counter = my_counter.count(50,5)
    n = next(counter)
    while n <= end:
        print(n, end = ' ')
        n = next(counter)

    print("\n")

    print("Count_end end = 100, start = 50, step = 5:")

    for n in my_counter.count_end(end,50,5):
        print(n, end = ' ')

    print("\n")

    print("list(zip(range(20), my_counter.count(50,5))):")

    print(list(zip(range(20), my_counter.count(50,5))))

    print()

    print("Count_ntimes ntimes = 20, start = 50, step = 5:")

    for n in my_counter.count_ntimes(20,50,5):
        print(n, end = ' ')

    print("\n")

    print("list(my_counter.count_end(10)):")
    print(list(my_counter.count_end(10)))

    print()

    print('''list(map("{:02d}".format, my_counter.count_end(10,1))):''')
    print(list(map("{:02d}".format, my_counter.count_end(10,1))))

    print()

    print('''counter = map("{:02d}".format, my_counter.count(1))\nlist(zip(range(1,11), counter))):''')
    counter = map("{:02d}".format, my_counter.count(1))
    print(list(zip(range(1,11), counter)))

    print()

    print("my_counteronacci:")
    for n in my_counter.fib(1000):
        print(n, end = ' ')

    print()

    aaa = list(my_counter.fib(1000))
    print (aaa)
    print()
    for a in aaa:
        print (a)
    print()
    for i in range(len(aaa)):
        print (aaa[i])

    print(list(map("{:02}".format, my_counter.fib(100))))
    print(list(map(lambda x: x, my_counter.fib(100))))

    counter = map("{}".format, my_counter.count_end(2))
    print(next(counter))
    print(next(counter))
    print(next(counter))
    try:
        print(next(counter))    # the same as raise StopIteration in iterator
    except Exception as e:
        print(type(e))

    print()

    counter = map("{}".format, my_counter.count_end(2))
    while True:
        try:
            print(next(counter))
        except StopIteration:
            print("Finish!")
            break


    input("Press enter to quit")
