import pytest
from main import GroupAnagram

class TestClass:

    def test_1(self):
        x = GroupAnagram.solution(["eat","tea","tan","ate","nat","bat"])
        assert x == [["bat"],["nat","tan"],["ate","eat","tea"]]
