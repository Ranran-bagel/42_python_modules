# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/22 10:59:51 by wezhou            #+#    #+#              #
#    Updated: 2026/05/22 11:02:49 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_harvest_total():
	day_01 = int(input("Day 1 harvest: "))
	day_02 = int(input("Day 2 harvest: "))
	day_03 = int(input("Day 3 harvest: "))
	har_total = day_01 + day_02 + day_03
	print(f"Total harvest: {har_total}")
 