import sys


def main() -> None:
    arg_count = len(sys.argv)
    arg_number = 1
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if arg_count == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arg_count - 1}")
        for arg in sys.argv[1:]:
            print(f"Argument {arg_number}: {arg}")
            arg_number += 1
    print(f"Total arguments: {arg_count}")


if __name__ == "__main__":
    main()
