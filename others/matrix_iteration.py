matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# nested for

for elt in matrix:
    for nested_elt in elt:
        print(f"nested for case {nested_elt}")


# nested while

i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[i]):
        print(f"nested while {matrix[i][j]}")
        j += 1
    i += 1


# using borders. spiral list parsing
# 1 - 2 - 3
# 4 - 5 - 6
# 7 - 8 - 9

# expected: 1, 2, 3, 6, 9, 8, 7, 4, 5

left = 0
top = 0
right = len(matrix[0])
bottom = right

while left < right and top < bottom:
    # print(f"left:{left}, right:{right}, top:{top}, bottom:{bottom}")
    for i in range(left, right):
        print(f"snail  {matrix[top][i]}")
    top += 1
    # print(f"left:{left}, right:{right}, top:{top}, bottom:{bottom}")

    for i in range(top, bottom):
        print(f"snail2 {matrix[i][right-1]}")
    right -= 1

    # print(f"left:{left}, right:{right}, top:{top}, bottom:{bottom}")
    for i in range(right - 1, left - 1, -1):
        print(f"snail3: {matrix[bottom-1][i]}")
    bottom -= 1

    # print(f"left:{left}, right:{right}, top:{top}, bottom:{bottom}")
    for i in range(bottom - 1, top - 1, -1):
        # print(f"i{i}")
        print(f"snail4: {matrix[i][left]}")
    left += 1
    # break
