from fibonacci import fibo3

def test_fibo3_when_0_item():
    elements = list(fibo3(0))
    assert elements == []

def test_fibo3_when_1_item():
    elements = list(fibo3(1))
    assert elements == [0]

def test_fibo3_when_2_items():
    elements = list(fibo3(2))
    assert elements == [0, 1]

def test_fibo3_when_n_items():
    elements = list(fibo3(6))
    assert elements == [0, 1, 1, 2, 3, 5]
