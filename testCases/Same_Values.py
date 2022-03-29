from updatedSort import *
git_sort = TestBubbleSortAlgorithm()


def test_bubble_sort_same_numbers():
    input_list = [1, 1, 1, 1]
    git_sort._test_sort(bubble_sort_v1, input_list)
