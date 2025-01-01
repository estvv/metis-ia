import typing

class Vector:
    x: int = 0
    y: int = 0

    @typing.overload
    def __init__(self, __x__: int, __y__: int) -> None: ...
    @typing.overload
    def __init__(self, __tuple__: tuple) -> None: ...

    def __init__(self, *args) -> None:
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 1 and isinstance(args[0], tuple):
            self.x, self.y = args[0]
        else:
            self.x = 0
            self.y = 0

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other: "Vector") -> bool:
        return self.x == other.x and self.y == other.y

    def update(self, x: int, y: int):
        self.x, self.y = x, y
