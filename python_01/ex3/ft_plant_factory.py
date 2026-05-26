# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/26 12:12:30 by wezhou            #+#    #+#              #
#    Updated: 2026/05/26 12:24:17 by wezhou           ###   ########.fr        #
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
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()
