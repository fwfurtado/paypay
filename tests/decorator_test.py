import pytest

def math(operator):
    def inner(a, b):
        return operator(a, b)

    return inner


def log(func):
    def inner(*args):
        print(f"Given args: {args}")
        print(f"Calling function {func.__name__}")
        return func(*args)

    return inner


def printX(a, b):
    print(a)
    print(b)
    return a, b


def sub(a, b):
    return a - b


@log
def soma(a, b):
    return a + b


def test_math():
    # log_soma = log(soma)
    print()
    print(soma(2, 3))


def test_soma():
    a = 1
    b = 2
    assert 3 == soma(a, b)


class Test:

    @property
    def blah(self):
        return 1

    @blah.setter
    def set_blah(self, new):
        self.xpto = new
        return new

    def __getattribute__(self, item):
        if item == "blah":
            return self.blah()

@pytest.mark.skip()
def test_test():
    t = Test()
    t.blah = 2