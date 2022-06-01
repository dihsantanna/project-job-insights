import pytest
from src.counter import count_ocurrences

path = "src/jobs.csv"
word1 = "Python"
word2 = "Javascript"


def test_counter():
    assert count_ocurrences(path, word1) == 1639

    assert count_ocurrences(path, word2) == 122

    with pytest.raises(AssertionError):
        assert count_ocurrences(path, word1) == 122
        assert count_ocurrences(path, word2) == 1639
