# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/19 11:47:28 by wezhou            #+#    #+#              #
#    Updated: 2026/06/19 20:47:02 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

TOTAL_ACHI = ["First Steps",
	"Master Explorer",
	"Boss Slayer",
	"Treasure Hunter",
	"Speed Runner",
	"Crafting Genius",
	"World Savior",
	"Collector Supreme",
	"Untouchable",
	"Strategist",
	"Survivor",
	"Unstoppable",
	"Sharp Mind",
	"Hidden Path Finder",]

MIN_ACHI_PER_PLAYER = 5
MAX_ACHI_PER_PLAYER = 8


def gen_player_achievements() -> set[str]:
    count = random.randint(
        MIN_ACHI_PER_PLAYER,
        MAX_ACHI_PER_PLAYER,)
    play_achi = random.sample(TOTAL_ACHI, count)
    return set(play_achi)


def  main() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print("=== Achievement Tracker System ===")
    print()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    distinct_achi = alice.union(bob.union(charlie.union(dylan)))
    print(f"All distinct achievements: {distinct_achi}")
    print()
    common_achi = alice.intersection(bob.intersection(charlie.intersection(dylan)))
    print(f"Common achievements: {common_achi}")
    print()
    only_Alice = alice.difference(bob.union(charlie.union(dylan)))
    only_Bob = bob.difference(alice.union(charlie.union(dylan)))
    only_Charlie = charlie.difference(alice.union(bob.union(dylan)))
    only_Dylan = dylan.difference(alice.union(bob.union(charlie)))
    print(f"Only Alice has: {only_Alice}")
    print(f"Only Bob has: {only_Bob}")
    print(f"Only Charlie has: {only_Charlie}")
    print(f"Only Dylan has: {only_Dylan}")
    print()
    print(f"Alice is missing: {set(TOTAL_ACHI).difference(alice)}")
    print(f"Bob is missing: {set(TOTAL_ACHI).difference(bob)}")
    print(f"Charlie is missing: {set(TOTAL_ACHI).difference(charlie)}")
    print(f"Dylan is missing: {set(TOTAL_ACHI).difference(dylan)}")


if __name__ == "__main__":
    main()
