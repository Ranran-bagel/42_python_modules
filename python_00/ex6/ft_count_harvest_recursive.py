# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/22 11:28:23 by wezhou            #+#    #+#              #
#    Updated: 2026/05/22 20:54:29 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_helper_recursive(n: int):
	if n <= 1:
		print(f"Day {n}")
		return
	ft_helper_recursive(n - 1)
	print(f"Day {n}")
	

def	ft_count_harvest_recursive():
	until_har = int(input("Days until harvest: "))
	ft_helper_recursive(until_har)
	print("Harvest time!")
