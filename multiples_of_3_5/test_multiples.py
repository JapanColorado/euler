from multiples import multiples_3_5

def test_10():
    '''Test for value of 10.'''
    result = multiples_3_5(10)
    expected = 23
    assert result == expected