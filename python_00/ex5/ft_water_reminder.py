# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/22 11:11:35 by wezhou            #+#    #+#              #
#    Updated: 2026/05/22 11:18:12 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	wa_inter = int(input("Days since last watering: "))
	if wa_inter > 2:
		print("Water the plants!")
	else:
		print("Plants are fine")
  