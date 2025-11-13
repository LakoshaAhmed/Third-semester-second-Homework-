from dataclasses import dataclass, asdict
from typing import Dict, Any
class Address:
    def __new__(cls, city, street, house_no):
        if not isinstance(city, str):
            raise TypeError("city must be a string")
        if not isinstance(street, str):
            raise TypeError("street must be a string")
        if not isinstance(house_no, int):
            raise TypeError("house_no must be an integer")

        self = super().__new__(cls)
        self.__dict__["city"] = city
        self.__dict__["street"] = street
        self.__dict__["house_no"] = house_no
        return self  

    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError(f"Cannot modify immutable attribute '{name}'")
        else:
            super().__setattr__(name, value)

    def __repr__(self):
        return f"Address(city={self.city!r}, street={self.street!r}, house_no={self.house_no})"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "city": self.city,
            "street": self.street,
            "house_no": self.house_no
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Address":
        return cls(data["city"], data["street"], data["house_no"])



@dataclass
class Person:
    name: str
    last_name: str
    patronymic: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Person":
        return cls(**data)



@dataclass
class Transaction:
    amount: float
    person: Person

    def __repr__(self):
        sign = "+" if self.amount >= 0 else "-"
        return f"Transaction({sign}{abs(self.amount)}, person={self.person.last_name} {self.person.name})"
    

    
