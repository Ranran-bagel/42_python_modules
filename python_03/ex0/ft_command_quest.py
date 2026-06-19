# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/18 14:10:12 by wezhou            #+#    #+#              #
#    Updated: 2026/06/19 14:01:18 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def  main() -> None:
    ar_num = len(sys.argv)
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if (ar_num) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {ar_num - 1}")
        for arg in sys.argv[1:]:
            print(f"Argument 1: {arg}")
    print(f"Total arguments: {ar_num}")


if __name__ == "__main__":
    main()
