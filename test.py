import pytest
from square import utils

class test_square_area:

    def test_compute(self):
        assert util.standard_deviation(5) == 25

    def test_many_numbers(self):
        with pytest.raises(TypeError):
            util.standard_deviation([1,2,3])

    def test_character(self):
        with pytest.raises(TypeError):
            util.standard_deviation("hi there")

    def test_empty(self):
        with pytest.raises(TypeError):
            util.standard_deviation([])
