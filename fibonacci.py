def fibo_inf():
    n1 = 0
    n2 = 1
    yield n1
    yield n2
    while True:
        n1, n2 = n2, n1 + n2
        yield n2

def fibo(n: int):
    yield from (v for v, _ in zip(fibo_inf(), range(n)))

def fibo2(n: int):
    g = fibo_inf()
    for _ in range(n):
        yield next(g)

def fibo3(n: int):
    n1 = 0
    n2 = 1
    if n > 0:
        yield n1
    if n > 1:
        yield n2
    for _ in range(n-2):
        n1, n2 = n2, n1 + n2
        yield n2