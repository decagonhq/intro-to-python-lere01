class loop_through_one_billion:

    def __init__(self):
        self.i = 0
        self.stop = 1000000000

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.stop:
            start = self.i + 1
            self.i += 1
            return start
        else:
            raise StopIteration()


def generator():
    n = 1

    while n <= 1000000000:
        yield n
        n += 1
