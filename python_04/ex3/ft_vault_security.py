def secure_archive(file_name: str, action: str = "r", content: str = "") -> tuple[bool, str]:
    if action not in ["r", "w"]:
        return (False, "Unknown archive action")
    try:
        with open(file_name, action) as file:
            if action == "r":
                return (True, file.read())
            else:
                file.write(content)
                return (True, "Content successfully written to file")
    except OSError as error:
        return (False, f"{error}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    nonexistent_file = secure_archive("/not/existing/file", "r")
    print(nonexistent_file)
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    inaccessible_file = secure_archive("/etc/master.passwd", "r")
    print(inaccessible_file)
    print()
    print("Using 'secure_archive' to read from a regular file:")
    regular_file = secure_archive("fragment.txt", "r")
    print(regular_file)
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    if regular_file[0]:
        written_file = secure_archive("new_file.txt", "w", regular_file[1])
        print(written_file)
    else:
        print("No content to write.")



if __name__ == "__main__":
    main()
