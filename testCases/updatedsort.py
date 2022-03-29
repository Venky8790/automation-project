import copy
import unittest


class TestBubbleSortAlgorithm(unittest.TestCase):
    @staticmethod
    def _test_sort(sorting_func, input_list):
        expected_list = sorted(input_list)
        assert sorting_func(input_list) == expected_list

    @staticmethod
    def bubble_sort_v1(container: object) -> object:
        # setting up variables

        container = list(copy.copy(container))
        length = len(container)

        while length:

            for i in range(len(container) - 1):
                if container[i] > container[i + 1]:
                    container[i], container[i + 1] = container[i + 1], container[i]

            length -= 1

        return container
