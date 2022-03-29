from updatedSort import *
git_sort = TestBubbleSortAlgorithm()


def test_bubble_sort_with_positive_numbers():
    input_list = [5, 5, 7, 8, 2, 4, 1]
    git_sort._test_sort(bubble_sort_v1, input_list)
