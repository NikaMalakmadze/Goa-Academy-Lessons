# 1) შექმენი მანქანის კლასი რომელსაც ექნება ატრიბუტებად ბრენდი მოდელი და წელი, დაამატე დამატებითი მეთოდი რომელიდ ამ ინფორმაციას დაბეჭდავს

class Car:
	"""Very Simple Car Class"""
	def __init__(self, brand: str, model: str, year: int) -> None:
		self.brand: str = brand
		self.model: str = model
		self.year: int = year	

	def info(self) -> None:
		info_dict: dict[str, str | int] = {
			'brand': self.brand,
			'model': self.model,
			'year': self.year
		}
		print(info_dict)

car: Car = Car('Mercedes', 'CLS', 2016)

car.info()

# შექმენი user კლასი რომელსაც ექნება ატრიბუტებად სახელი და ასაკი და დაბეჭდე ასე რომ 'მე ვარ "სახელი" "ამდენი" წლის

class User:
	def __init__(self, name: str, age: int) -> None:
		self.name: str = name
		self.age: int = age

	def info(self) -> None:
		info_str: str = f'I am {self.name}, {self.age} old.'
		print(info_str)

user: User = User('Nika', 16)

user.info()