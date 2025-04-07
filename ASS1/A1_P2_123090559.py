def solve():
    n, q = map(int, input().split())
    permutation = list(map(int, input().split()))
    left = list(map(int, input().split()))[:q]
    right = list(map(int, input().split()))[:q]
    numbers = {val: index for index, val in enumerate(permutation)}

    for i in range(q):
        left[i], right[i] = numbers[left[i]], numbers[right[i]]

    if left[0] != 0 or right[0] != n - 1:
        return 0

    record = [0] * n
    left_map = {}

    for i in range(q):
        left_index = left[q - 1 - i]
        right_index = right[q - 1 - i]

        if left_index >= right_index:
            return 0

        if record[left_index] == 1:
            if left_index not in left_map:
                return 0
            else:
                if right_index <= left_map[left_index]:
                    return 0
                else:
                    for k in range(left_map[left_index], right_index + 1):
                        record[k] = 1
        else:
            for k in range(left_index, right_index + 1):
                if record[k] != 1:
                    record[k] = 1
                else:
                    if left_map[k] != right_index:
                        return 0
                    else:
                        break
        left_map[left_index] = right_index

    return 1


if solve() == 1:
    print(1)
else:
    print(0)