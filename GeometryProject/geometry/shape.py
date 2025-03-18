
from dataclasses import dataclass


@dataclass(kw_only=True)
class Shape:
    name: str | None = None # since python 3.10 (before: typing.Optional[str])