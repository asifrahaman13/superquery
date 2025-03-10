from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    def __str__(self):
        return self.value


print(Color.RED)
print(type(Color.RED))

if "red" == Color.RED:
    print("Equal")
else:
    print("Not Equal")
