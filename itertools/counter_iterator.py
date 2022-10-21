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


class MyCounter2:
    def __init__(self, ntimes, start = 0, step = 1):
        self.ntimes = ntimes  # just for info
        end = start + step * ntimes
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


class MyFibonacci:

    def __init__(self, end):
        self.a, self.b = 0, 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        a, b = self.a, self.b
        if a > self.end:
            raise StopIteration
        self.a, self.b = b, a + b
        return a


if __name__ == "__main__":

    end = 10
    counter1 = MyCounter1(end)
    print("counter1 = MyCounter1(end):")
    print("class", counter1.__class__)
    print(next(counter1))
    print(next(counter1))
    for i in counter1:
        print(i)
    print()

    ntimes = 10
    counter2 = MyCounter2(ntimes)
    print("counter2 = MyCounter2(ntimes):")
    print("class", counter2.__class__)
    print(next(counter2))
    print(next(counter2))
    for i in counter2:
        print(i)
    print()

    counter3 = MyFibonacci(end)
    print("counter3 = MyFibonacci(end):")
    print("class", counter3.__class__)
    print(next(counter3))
    print(next(counter3))
    for i in counter3:
        print(i)
    print()

    input("Press enter to quit")
