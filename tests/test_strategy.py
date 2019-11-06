"""
Unit tests for ``strategy``.
"""
import unittest
import numpy
from strat_2048_rvk.strategy import (
    strategy, grid_score, not_equal
)
from strat_2048_rvk import evaluate_strategy, Game2048


class TestStrategy(unittest.TestCase):
    def test_grid_score(self):
        score = grid_score(numpy.zeros((4, 4), dtype=int))
        assert score >= 0

    def test_not_equal(self):
        temp1, temp2 = numpy.zeros((4, 4), dtype=int), numpy.zeros((4, 4), dtype=int)
        gen = not_equal(temp1, temp2)
        assert type(gen) == bool
        assert gen == False
        temp1[1][1] = 2
        gen = not_equal(temp1, temp2)
        assert type(gen) == bool
        assert gen == True

    def test_strategy(self):
        mat = numpy.zeros((4, 4), dtype=numpy.int32)
        mat[1, 1] = 1
        g = Game2048(mat)
        rnd = strategy(g.game, g.state, g.moves)
        assert rnd in {0, 1, 2, 3}

    def test_measure_strategy(self):
        gen = evaluate_strategy(strategy)
        res = list(gen)
        assert isinstance(res, list)
        assert all(map(lambda x: x > 0, res))

if __name__ == '__main__':
    unittest.main()
