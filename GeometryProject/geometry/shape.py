from dataclasses import dataclass


@dataclass(kw_only=True)
class Shape:
    """Represents a Shape with an optional name. 
    
    Provides a base class to build all sort of shapes with common properties and methods.
    """

    name: str | None = None # since python 3.10 (before: typing.Optional[str])

    def __str__(self):
        return "" if self.name is None else self.name

    def translate(self, delta_x: float, delta_y: float) -> None:
        pass