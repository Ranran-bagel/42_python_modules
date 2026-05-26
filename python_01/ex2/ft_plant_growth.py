# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/26 11:30:02 by wezhou            #+#    #+#              #
#    Updated: 2026/05/26 11:55:56 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant():
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age_days = age

    def show(self):
        print(f"{self.name}: {self.height:g}cm, {self.age_days} days old")

    def age(self, time: int):
        self.age_days += time

    def grow(self, growth_rate: float):
        for i in range(7):
            self.height += growth_rate
            self.age(1)
            print(f"=== Day {i + 1} ===")
            print(f"{self.name}: {round(self.height, 1)}cm, {self.age_days} days old")
        week_growth = growth_rate * 7
        print(f"Growth this week: {round(week_growth, 1)}cm")

if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    rose.grow(0.8)
    