from bigproject.mylib import sinusoides


def test_sinusoides():
    x, y1, y2 = sinusoides(2, 1_000_000)
    assert 1_000_000 == len(x)
    assert 1_000_000 == len(y1)
    assert 1_000_000 == len(y2)