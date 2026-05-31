# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wezhou <wezhou@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/27 19:14:57 by wezhou            #+#    #+#              #
#    Updated: 2026/05/27 19:48:24 by wezhou           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant():
	def __init__(self, name: str, height: float, age: int):
		self._name = name
		self._height = height
		self._age_days = age

	def show(self):
		print(f"{self._name}: {self._height:g}cm, {self._age_days} days old")

	def age(self, time: int):
		self._age_days += time

	def grow(self, growth_rate: float):
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

	def	set_height(self, height: float):
		if height < 0:
			print(f"{self._name}: Error, height can't be negative")
			print("Height update rejected")
			return
		self._height = height
		print(f"Height updated: {round(self._height, 1)}cm")

	def	set_age(self, age: int):
		if age < 0:
			print(f"{self._name}: Error, age can't be negative")
			print("Age update rejected")
			return
		self._age_days = age
		print(f"Age updated: {self._age_days}cm")

class Flower(Plant):
	def	__init__(self, name:str, height:float, age:int, color:str, has_bloomed:bool):
		super().__init__(name, height, age)
		self._color = color
		self._has_bloomed = has_bloomed

	def bloom(self):
		if self._has_bloomed == True:
			return
		else:
			self._has_bloomed = True
	
	def	show(self)
		super().show()
		print(f"Color: {self._color}")
		if self._has_bloomed == True:
			print("Rose is blooming beautifully!")
		else:
			print("Rose has not bloomed yet")

class Tree():
	def	__init__(self, name:str, height:float, age:int, trunk_diameter:float)
		super().__init__(name, height, age)
		self._trunk_diameter = trunk_diameter

	def	produce_shade(self)
		print(f"Tree {self._name} now produces a shade of {round(self._height, 1)}cm long and {round(self._trunk_diameter, 1)}cm wide.")

	def	show(self):
		super().show()
		print(f"Trunk diameter: {round(self._trunk_diameter)}cm")

class Vegetable():
	def	__init__(self, name:str, height:float, age:int, harvest_season:str, nutritional_value:int):
		super().__init__(name, height, age)
		self._harvest_season = harvest_season
		self._nutritional_value = nutritional_value

	def show(self)
if __name__ == "__main__":
	