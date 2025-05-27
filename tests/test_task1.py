import pytest

from task1.solution import sum_two


@pytest.mark.parametrize(
    'a, b',
    [
        (1, '2'),
        ('1', 2),
        ('1', '2'),
        (None, 2),
        (1.2, 2),
        (1, 2.1),
        (True, 2),
        (1, False),
    ]
)
def test_sum_two_invalid_types(a, b):
    with pytest.raises(TypeError):
        sum_two(a, b)


@pytest.mark.parametrize(
    'a, b, expected',
    [
        (1, 2, 3),
        (3, 4, 7),
    ]
)
def test_sum_two(a, b, expected):
    assert sum_two(a, b) == expected
