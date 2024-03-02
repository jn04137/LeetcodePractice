import pytest
from main import Solution

class TestClass:

    def test_one(self):
        result = Solution.topKFrequent([1,1,1,2,2,3], 2)
        assert set(result) == set([2,1])

    def test_two(self):
        result = Solution.topKFrequent([1], 1)
        assert set(result) == set([1])

    def test_three(self):
        result = Solution.topKFrequent([4,1,-1,2,-1,2,3], 2)
        assert set(result) == set([-1,2])

    def test_four(self):
        result = Solution.topKFrequent([-1,-1], 1)
        assert set(result) == set([-1])
