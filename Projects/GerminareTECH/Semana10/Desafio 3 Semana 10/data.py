from dataclasses import dataclass,field

@dataclass
class data:
    afabeto = [
            {"word": "a", "value": 0},
            {"word": "b", "value": 0},
            {"word": "c", "value": 0},
            {"word": "d", "value": 0},
            {"word": "e", "value": 0},
            {"word": "f", "value": 0},
            {"word": "g", "value": 0},
            {"word": "h", "value": 0},
            {"word": "i", "value": 0},
            {"word": "j", "value": 0},
            {"word": "k", "value": 0},
            {"word": "l", "value": 0},
            {"word": "m", "value": 0},
            {"word": "n", "value": 0},
            {"word": "o", "value": 0},
            {"word": "p", "value": 0},
            {"word": "q", "value": 0},
            {"word": "r", "value": 0},
            {"word": "s", "value": 0},
            {"word": "t", "value": 0},
            {"word": "u", "value": 0},
            {"word": "v", "value": 0},
            {"word": "w", "value": 0},
            {"word": "x", "value": 0},
            {"word": "y", "value": 0},
            {"word": "z", "value": 0},
        ]
    
    select_word: list[str] = field(default_factory=list)