import pytest
from main import Solution


class TestClass:

    def test_one(self):
        result = Solution.longestConsecutive([100,4,200,1,3,2])
        assert result == 4

    def test_two(self):
        result = Solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])
        assert result == 9
