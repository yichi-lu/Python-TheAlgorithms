"""
This is a pure Python implementation of the merge sort algorithm.

For doctests run following command:
python -m doctest -v merge_sort.py
or
python3 -m doctest -v merge_sort.py
For manual testing run:
python merge_sort.py
"""

"""
example:
Enter numbers separated by a comma:
7,6,5,4,3,2,1
merge_sort. mid index: 3, collection: [7, 6, 5, 4, 3, 2, 1]
merge_sort. mid index: 1, collection: [7, 6, 5]
merge_sort. mid index: 1, collection: [6, 5]
merge. left len: 1, left: [6], right len: 1, right: [5]
merge. #1, result: [5]
merge. #2, result: [5, 6]
merge. #3, result: [5, 6]
merge. left len: 1, left: [7], right len: 2, right: [5, 6]
merge. #1, result: [5]
merge. #1, result: [5, 6]
merge. #2, result: [5, 6, 7]
merge. #3, result: [5, 6, 7]
merge_sort. mid index: 2, collection: [4, 3, 2, 1]
merge_sort. mid index: 1, collection: [4, 3]
merge. left len: 1, left: [4], right len: 1, right: [3]
merge. #1, result: [3]
merge. #2, result: [3, 4]
merge. #3, result: [3, 4]
merge_sort. mid index: 1, collection: [2, 1]
merge. left len: 1, left: [2], right len: 1, right: [1]
merge. #1, result: [1]
merge. #2, result: [1, 2]
merge. #3, result: [1, 2]
merge. left len: 2, left: [3, 4], right len: 2, right: [1, 2]
merge. #1, result: [1]
merge. #1, result: [1, 2]
merge. #2, result: [1, 2, 3, 4]
merge. #3, result: [1, 2, 3, 4]
merge. left len: 3, left: [5, 6, 7], right len: 4, right: [1, 2, 3, 4]
merge. #1, result: [1]
merge. #1, result: [1, 2]
merge. #1, result: [1, 2, 3]
merge. #1, result: [1, 2, 3, 4]
merge. #2, result: [1, 2, 3, 4, 5, 6, 7]
merge. #3, result: [1, 2, 3, 4, 5, 6, 7]
1,2,3,4,5,6,7
"""

def merge_sort(collection: list) -> list:
    """
    Sorts a list using the merge sort algorithm.

    :param collection: A mutable ordered collection with comparable items.
    :return: The same collection ordered in ascending order.

    Time Complexity: O(n log n)

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    def merge(left: list, right: list) -> list:
        """
        Merge two sorted lists into a single sorted list.

        :param left: Left collection
        :param right: Right collection
        :return: Merged result
        """
        result = []
#       print(f"merge. left len: {len(left)}, left: {left}, right len: {len(right)}, right: {right}")
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
#           print(f"merge. #1, result: {result}")
        result.extend(left)
#       print(f"merge. #2, result: {result}")
        result.extend(right)
#       print(f"merge. #3, result: {result}")
        return result

    if len(collection) <= 1:
        return collection
    mid_index = len(collection) // 2
#   print(f"merge_sort. mid index: {mid_index}, collection: {collection}")
    return merge(merge_sort(collection[:mid_index]), merge_sort(collection[mid_index:]))


if __name__ == "__main__":
    import doctest

#   doctest.testmod()

    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",")]
        sorted_list = merge_sort(unsorted)
        print(*sorted_list, sep=",")
    except ValueError:
        print("Invalid input. Please enter valid integers separated by commas.")
