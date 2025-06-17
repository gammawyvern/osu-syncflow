from dataclasses import dataclass

@dataclass
class TimingPoint:
    time: int
    beatLength: float
    meter: int
    sampleSet: int
    sampleIndex: int
    volume: int
    uninherited: bool
    effect: int

