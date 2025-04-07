def update(inp, k, x, y, c, P):
    return ((x * x + k * y + 5 * x) % P) * c


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    P = int(data[idx + 2])
    idx += 3

    a = []
    sum_ = 0
    count = 0
    countArr = [0] * P

    for i in range(n):
        inp = int(data[idx])
        idx += 1
        sum_ += inp
        a.append(inp)

    for value in a:
        countArr[abs(value)] += 1

    if countArr[0] != 0:
        count += 1

    for i in range(1, P):
        if countArr[i] == 0:
            pass
        elif countArr[i] == 1:
            count += 1
        else:
            count += 2

    for _ in range(m):
        inp = int(data[idx])
        idx += 1
        if inp == 1:
            k = int(data[idx]) - 1
            x = int(data[idx + 1])
            y = int(data[idx + 2])
            c = int(data[idx + 3])
            idx += 4

            sum_ -= a[k]

            countArr[abs(a[k])] -= 1
            if a[k] == 0:
                if countArr[0] == 0:
                    count -= 1
            else:
                if countArr[abs(a[k])] == 1 or countArr[abs(a[k])] == 0:
                    count -= 1

            a[k] = update(a[k], k + 1, x, y, c, P)
            sum_ += a[k]

            countArr[abs(a[k])] += 1
            if a[k] == 0:
                if countArr[0] == 1:
                    count += 1
            else:
                if countArr[abs(a[k])] == 1 or countArr[abs(a[k])] == 2:
                    count += 1

        elif inp == 2:
            print(sum_)

        elif inp == 3:
            print(count)

        else:
            return


if __name__ == "__main__":
    main()
