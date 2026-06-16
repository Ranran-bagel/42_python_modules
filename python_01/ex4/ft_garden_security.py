# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/27 18:43:26 by wezhou            #+#    #+#              #
#    Updated: 2026/06/01 13:21:17 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age_days = age

    def show(self) -> None:
        print(f"{self._name}: {self._height:g}cm, {self._age_days} days old")

    def age(self, time: int) -> None:
        self._age_days += time

    def grow(self, growth_rate: float) -> None:
        for i in range(7):
            self._height += growth_rate
            self.age(1)
            print(f"=== Day {i + 1} ===")
            print(f"{self._name}: {round(self._height, 1)}cm, {self._age_days} days old")
        week_growth = growth_rate * 7
        print(f"Growth this week: {round(week_growth, 1)}cm")

    def	get_height(self) -> float:
        return self._height

    def	get_age(self) -> int:
        return self._age_days

    def	set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {round(self._height, 1)}cm")

    def	set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age_days = age
        print(f"Age updated: {self._age_days}cm")

if __name__ == "__main__":
    print("=== Garden Security System ===")
    print("Plant created: ", end = "")
    rose = Plant("Rose", 15, 10)
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-1)
    rose.set_height(-10)
    print()
    print("Current state: ", end = "")
    rose.show()
