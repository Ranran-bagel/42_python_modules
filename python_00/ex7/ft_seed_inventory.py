# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/22 21:03:50 by wezhou            #+#    #+#              #
#    Updated: 2026/05/22 21:20:16 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit not in {"packets", "grams", "area"}:
		print("Unknown unit type")
		return
	if unit == "packets":
		print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
	elif unit == "grams":
		print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
	else:
		print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
	
