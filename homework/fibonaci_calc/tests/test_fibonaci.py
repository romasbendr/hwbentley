from ..fibonaci import get_nth_member

def test_fibonaci_17():
    assert get_nth_member(17) == 1597

def test_fibonaci_20():
    assert get_nth_member(20) != "6765"