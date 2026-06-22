# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ancient_text.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/19 21:12:23 by wezhou            #+#    #+#              #
#    Updated: 2026/06/20 21:24:48 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import typing


def read_file(file_name: str) -> typing.IO[str] | None:
    try:
        file = open(file_name, "r")
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        return
    return file


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    file = read_file(sys.argv[1])
    if file is None:
        return
    print("---")
    print()
    print(file.read(), end="")
    print()
    print("---")
    file.close()
    print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
