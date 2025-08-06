from __future__ import annotations
from dataclasses import dataclass
from typing import List

@dataclass
class TimingPoint:
    time: int
    beat_length: float
    meter: int
    uninherited: bool

    @staticmethod
    def from_line(line: str) -> TimingPoint:
        values: List[str] = line.split(',')
        if len(values) != 8:
            raise Exception(f"Timing point line was incorrect: {values}")

        return TimingPoint(
            time=int(values[0]),
            beat_length=float(values[1]),
            meter=int(values[2]),
            uninherited=bool(int(values[6])),
        )
