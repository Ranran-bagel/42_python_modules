import sys
import typing


def open_file(file_name: str) -> typing.IO[str] | None:
    try:
        file = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return None
    return file


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    file = open_file(file_name)
    if file is None:
        return
    try:
        content = file.read()
        print("---")
        print()
        print(content, end="")
        if content == "" or content[-1] != "\n":
            print()
        print()
        print("---")
    finally:
        file.close()
        print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
