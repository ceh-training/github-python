import sys

arguments: list[int] = []


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    while True:
        line = input()
        if not line:
            break
        for segment in line.split():
            try:
                arg = int(segment)
                arguments.append(arg)
            except ValueError as e:
                eprint(f"invalid argument: '{segment}'; {e}")

    print(sum(arguments))


if __name__ == "__main__":
    main()
