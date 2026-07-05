import sys
import typing


def read_file(file_name: str) -> typing.IO[str] | None:
    try:
        file = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        print("Data not saved.")
        return None
    return file


def save_file(file_name: str, new_content: str) -> bool:
    try:
        file = open(file_name, "w")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return False
    file.write(new_content)
    file.close()
    return True
    


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    file = read_file(sys.argv[1])
    if file is None:
        return
    print("---")
    print()
    content = file.read()
    print(content, end="")
    print()
    print("---")
    file.close()
    print(f"File '{sys.argv[1]}' closed.")
    print()
    new_content = content.replace("\n", "#\n")
    print("Transform data:")
    print("---")
    print()
    print(new_content, end="")
    print()
    print("---")
    file_name = input("Enter new file name (or empty): ")
    if not file_name:
        print("Not saving data.")
        return
    else:
        print(f"Saving data to '{file_name}'")
        is_saved = save_file(file_name, new_content)
        if is_saved:
            print(f"Data saved in file '{file_name}'.")
        else:
            return


if __name__ == "__main__":
    main()
