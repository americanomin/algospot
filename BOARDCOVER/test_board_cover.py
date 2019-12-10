import pytest

from BOARDCOVER.board_cover_leejimin import get_number_of_ways


class TestBoardCover(object):
    def test_get_number_of_ways_one_case(self):
        matrix = [
            [False, True, True, True, True, True, False],
            [False, True, True, True, True, True, False],
            [False, False, True, True, True, False, False],
        ]

        result = get_number_of_ways(matrix)
        assert result == 0

    def test_get_number_of_ways_two_case(self):
        matrix = [
            [False, True, True, True, True, True, False],
            [False, True, True, True, True, True, False],
            [False, False, True, True, False, False, False],
        ]

        result = get_number_of_ways(matrix)
        assert result == 2

    # def test_get_number_of_ways_three_case(self):
    #     matrix = [
    #         [False, False, False, False, False, False, False, False, False, False],
    #         [False, True, True, True, True, True, True, True, True, False],
    #         [False, True, True, True, True, True, True, True, True, False],
    #         [False, True, True, True, True, True, True, True, True, False],
    #         [False, True, True, True, True, True, True, True, True, False],
    #         [False, True, True, True, True, True, True, True, True, False],
    #         [False, True, True, True, True, True, True, True, True, False],
    #         [False, False, False, False, False, False, False, False, False, False]
    #     ]
    #     result = get_number_of_ways(matrix)
    #     assert result == 1514
