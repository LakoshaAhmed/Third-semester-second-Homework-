#Write a `validate` decorator that takes as input a class and an arbitrary number of pairs (attribute, validation function). 
# Before initializing an object,
#  you need to check all attributes from the pairs for correctness.



class ValidationException(Exception):
    pass


def validate(*validation_pairs):
    def decorator(cls):
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            original_init(self, *args, **kwargs)

            for attr, validator in validation_pairs:
                if not hasattr(self, attr):
                    raise ValidationException(f"Attribute '{attr}' not found in class {cls.__name__}.")
                value = getattr(self, attr)
                if not validator(value):
                    raise ValidationException(
                        f"Validation failed for attribute '{attr}' with value '{value}'."
                    )

        cls.__init__ = new_init
        return cls
    return decorator


def above_18(x):
    return x >= 18


@validate(("age", above_18))
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age


e1 = Employee("Jane Doe", 25)

e2 = Employee("John Don't", 15)
