# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_data.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/26 11:04:04 by wezhou            #+#    #+#              #
#    Updated: 2026/05/26 11:51:54 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant():
    def	__init__(self, name:str, height:float, age:int):
        self.name = name
        self.height = height
        self.age_days = age

    def	show(self):
        print(f"{self.name}: {self.height:g}cm, {self.age_days} days old")

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
    