# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_score_analytics.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/18 14:28:58 by wezhou            #+#    #+#              #
#    Updated: 2026/06/19 14:01:50 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def  main() -> None:
    score_lst = []
    print("=== Player Score Analytics ===")
    for arg in sys.argv[1:]:
        try:
            score_lst.append(int(arg))
        except:
            print(f"Invalid parameter: '{arg}'")
    if len(score_lst) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Total players: {len(score_lst)}")
        print(f"Average score: {sum(score_lst) / len(score_lst)}")
        print(f"High score: {max(score_lst)}")
        print(f"Low score: {min(score_lst)}")
        print(f"fScore range: {max(score_lst) - min(score_lst)}")


if __name__ == "__main__":
    main()
