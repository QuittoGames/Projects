from dataclasses import dataclass

@dataclass
class FilterParameters:
    name: str
    idade_min: int
    idade_max: int
    location: str
    value_min: float
