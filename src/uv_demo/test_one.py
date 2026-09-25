def inc(x):
    return x + 1


def test_inc_failed():
    assert inc(3) == 5


def test_inc_success():
    assert inc(3) == 4
