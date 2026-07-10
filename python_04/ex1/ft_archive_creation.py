import sys
import typing


def read_file(file_name: str) -> typing.IO[str] | None:
    try:
        file = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return None
    return file


def save_file(file_name: str, new_content: str) -> bool:
    try:
        file = open(file_name, "w")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return False
    try:
        file.write(new_content)
    except OSError as error:
        print(f"Error writing file '{file_name}': {error}")
        return False
    finally:
        file.close()
    return True


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    file = read_file(file_name)
    if file is None:
        return
    print("---")
    print()
    try:
        content = file.read()
        print(content, end="")
        if content == "" or content[-1] != "\n":
            print()
        print()
        print("---")
    except OSError as error:
        print(f"Error reading file '{file_name}': {error}")
        return
    finally:
        file.close()
        print(f"File '{file_name}' closed.")
    print()
    new_content = content.replace("\n", "#\n")
    if content != "" and content[-1] != "\n":
        new_content += "#"
    print("Transform data:")
    print("---")
    print()
    print(new_content, end="")
    if new_content == "" or new_content[-1] != "\n":
        print()
    print()
    print("---")
    file_name = input("Enter new file name (or empty): ")
    if not file_name:
        print("Not saving data.")
        return
    print(f"Saving data to '{file_name}'")
    is_saved = save_file(file_name, new_content)
    if is_saved:
        print(f"Data saved in file '{file_name}'.")


if __name__ == "__main__":
    main()
