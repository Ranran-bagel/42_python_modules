class Plant():
	def __init__(self, name: str, height: float, age: int) -> None:
		self.name = name
		self.height = height
		self.age_days = age

	def show(self) -> None:
		print(f"{self.name}: {self.height:g}cm, {self.age_days} days old")

	def age(self, time: int) -> None:
		self.age_days += time

	def grow(self, growth_rate: float) -> None:
		for i in range(7):
			self.height += growth_rate
			self.age(1)
		week_growth = growth_rate * 7
		print(f"Growth this week: {round(week_growth, 1)}cm")

if __name__ == "__main__":
	rose = Plant("Rose", 25, 30)
	print("=== Garden Plant Growth ===")
	rose.grow(0.8)
	