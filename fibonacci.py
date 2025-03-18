from collections.abc import Generator # since 3.10
# from typing import Generator # oldest version

def fibo_inf() -> Generator[int]:
    n1 = 0
    n2 = 1
    yield n1
    yield n2
    while True:
        n1, n2 = n2, n1 + n2
        yield n2

def fibo(n: int)  -> Generator[int]:
    yield from (v for v, _ in zip(fibo_inf(), range(n)))

def fibo2(n: int) -> Generator[int]:
    g = fibo_inf()
    for _ in range(n):
        yield next(g)

def fibo3(n: int) -> Generator[int]:
    n1 = 0
    n2 = 1
    if n > 0:
        yield n1
    if n > 1:
        yield n2
    for _ in range(n-2):
        n1, n2 = n2, n1 + n2
        yield n2


if __name__ == '__main__':
    generator = fibo3(10)
    print(generator)
    for v in generator:
        print(v)
    print(generator)