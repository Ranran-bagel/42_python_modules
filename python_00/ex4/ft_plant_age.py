# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/22 11:03:24 by wezhou            #+#    #+#              #
#    Updated: 2026/05/22 11:10:40 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plant_age():
	plant_age = int(input("Enter plant age in days: "))
	if plant_age > 60:
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
