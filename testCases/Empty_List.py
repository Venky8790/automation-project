from updatedSort import *
git_sort = TestBubbleSortAlgorithm()


def test_bubble_sort_empty_list():
    input_list = []
    git_sort._test_sort(bubble_sort_v1, input_list)
