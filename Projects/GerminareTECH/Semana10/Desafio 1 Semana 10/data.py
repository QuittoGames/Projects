from dataclasses import dataclass,field

@dataclass
class data:
    users = [
        {"name":"Grillo","endereco":"SP","Operadora":"Vivo"},
]
    screch_users = field(default_factory=list)