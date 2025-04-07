def process_case(n, instructions):
    complexity = 0
    max_complexity = 0
    whole = []
    loop_stack = []

    for i in range(n):
        line = instructions[i].strip().split()
        opt = line[0]

        if opt == "F":
            var = line[1]
            start = line[2]
            end = line[3]

            if end == "n" and start != "n":
                whole.append(1)
                loop_stack.append(1)
            else:
                whole.append(0)
                loop_stack.append(0)


        elif opt == "E":
            if loop_stack.pop() == 1:
                whole.append(-1)
            else:
                whole.append(0)

    for i in whole:
        complexity +=i
        if complexity > max_complexity:
            max_complexity = complexity


    if max_complexity != 0:
        print(f"O(n^{max_complexity})")
    else:
        print(f"O(1)")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        instructions = [input().strip() for _ in range(n)]
        process_case(n, instructions)


if __name__ == "__main__":
    main()
