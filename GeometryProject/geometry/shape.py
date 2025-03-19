from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import override


@dataclass(kw_only=True)
class Shape(ABC):
    """Represents a Shape with an optional name. 
    
    Provides a base class to build all sort of shapes with common properties and methods.
    """

    name: str | None = None # since python 3.10 (before: typing.Optional[str])

    @override # since 3.12
    def __str__(self) -> str:
        return "" if self.name is None else self.name

    @abstractmethod
    def translate(self, delta_x: float, delta_y: float) -> None:
        pass