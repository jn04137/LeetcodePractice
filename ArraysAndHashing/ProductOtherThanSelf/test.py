import pytest
from main import Product


class TestClass:

    def test_one(self):
        result = Product.optimized([1,2,3,4])
        assert result == [24,12,8,6]

    def test_two(self):
        result = Product.optimized([-1,1,0,-3,3])
        assert result == [0,0,9,0,0]
