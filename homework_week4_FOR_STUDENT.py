"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


def binary_search_matrix(matrix, target):
    result = []
    row = 0
    for i in matrix:
        low = 0
        high = len(i) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2 #this line gets the middle index of the array

            # If the target value is greater, this code means ignore left half
            if i[mid] < target:
                low = mid + 1

            # If the target value is smaller, ignore right half
            elif i[mid] > target:
                high = mid - 1

            # means the target value is present at middle index
            else:
                result.append(row)
                result.append(mid)
                return result
        row += 1

    return [-1,-1]


matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 44

final_result = binary_search_matrix(matrix, target)

if final_result != [-1, -1]:
    print("The target value is present at row {}, column {}".format(final_result[0], final_result[1]))
else:
    print("The target value tis not present in array")





