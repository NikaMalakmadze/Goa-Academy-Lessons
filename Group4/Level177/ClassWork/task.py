
from datetime import datetime

# 1) შექმენი ცხოველების კლასი და ამ კლასში შეინახე მათი სახელი, ჯიში, წელი, ფერი და საბოლოოდ ყველაფერი დაბეჭდე

class Animal():
    def __init__(
            self,
            name: str,
            breed: str,
            age: int,
            color: str
        ) -> None:
        self.name: str = name
        self.breed: str = breed
        self.age: int = age
        self.color: str = color

    def to_dict(self) -> dict[str, str | int]:
        return {
            'name': self.name,
            'breed': self.breed,
            'age': self.age,
            'color': self.color
        }

# task 2

class TimeMachine():
    def __init__(
            self, 
            current_age: int,
            current_year: int = datetime.now().year
        ) -> None:
        self.current_age: int = current_age
        self.current_year: int = current_year

    def back_to_future(self, years_to_travel: int) -> str:
        if not isinstance(years_to_travel, int) or years_to_travel < 0:
            raise ValueError('Invalid type or amount of years_to_travel argument')
        self.current_age += years_to_travel
        self.current_year += years_to_travel

        return f'Successfuly Traveled {years_to_travel} years in time!'

    def __str__(self) -> str:
        return f'Current Settings: \nCurrent Year: {self.current_year} \nCurrent Age: {self.current_age}'

time_machine = TimeMachine(16)
print(time_machine.back_to_future(10))
print(time_machine)
