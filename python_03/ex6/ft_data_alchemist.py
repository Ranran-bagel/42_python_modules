# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_alchemist.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/19 18:12:16 by wezhou            #+#    #+#              #
#    Updated: 2026/06/19 20:56:41 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    player_names = ['Alice', 'bob', 'Charlie',
                    'dylan', 'Emma', 'Gregory',
                    'john', 'kevin', 'Liam']
    capitalized_names = [name.capitalize() for name in player_names]
    capitalized_only = [name for name in player_names if name == name.capitalize()]
    print(f"Initial list of players: {player_names}")
    print(f"New list with all names capitalized: {capitalized_names}")
    print(f"New list of capitalized names only: {capitalized_only}")
    print()
    score_dict = {name: random.randint(0, 1000) for name in capitalized_names}
    average_score = round(sum(score_dict.values()) / len(score_dict), 2)
    high_scores = {name: score_dict[name] for
                   name in score_dict
                   if score_dict[name] > average_score}
    print(f"Score dict: {score_dict}")
    print(f"Score average is {average_score}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
