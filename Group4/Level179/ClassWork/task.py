
# 1) მოსწავლის რეგისტრაცია გოაში
# კლასი რომელსაც ექნება ატრიბუტები: სახელი, ასაკი, ჯგუფი, count რომელიც ითვლის რამდენი მოსწავლე არსებობს ჯამში

from dataclasses import dataclass


@dataclass
class Student:
	name: str
	age: int
	group: str

class Goa:
	__count: int = 0

	def __init__(self) -> None: self.students: list[Student] = []

	def add_member(self, name: str, age: int, group: str) -> int:
		self.students.append(Student(name, age, group))
		self.__count += 1
		return self.__count
	
	def get_count(self) -> int: return self.__count 

goa: Goa = Goa()

goa.add_member('Joe', 14, 'group 13')
goa.add_member('Emily', 12, 'group 11')
goa.add_member('Mia', 16, 'group 3')
current_count: int = goa.add_member('Bob', 13, 'group 6')

print(current_count)

print(goa.get_count())
