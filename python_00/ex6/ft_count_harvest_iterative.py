# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/22 11:22:41 by wezhou            #+#    #+#              #
#    Updated: 2026/05/22 11:28:05 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	until_har = int(input("Days until harvest: "))
	for i in range(1, until_har + 1):
		print(f"Day {i}")
	print("Harvest time!")
