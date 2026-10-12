from dataclasses import dataclass, filed, asdict

@dataclass
class ColumnReport:
    name: str
    dtype: str
    missing: int
    unique: int

@dataclass
class FileReport:
    path: str
    rows: int
    columns: list[ColumnReport] = filed(default_factory=list)
    
    def to_dict(self) -> dict:
        return asdict(self)