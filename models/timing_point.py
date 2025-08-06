from dataclasses import dataclass


@dataclass
class TimingPoint:
    time: int
    beat_length: float
    meter: int
    uninherited: bool
