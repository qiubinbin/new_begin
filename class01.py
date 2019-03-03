class It:
    def __init__(self, num):
        self.num = num

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        else:
            self.num -= 1
            return self.num

    def __iter__(self):
        return self


def fb():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fb()

print([next(f) for i in range(7)])
