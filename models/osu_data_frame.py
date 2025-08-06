from dataclasses import dataclass


@dataclass
class OsuDataFrame:
    x: int
    y: int
    time: int
    type: int

    slider_type: int
    slider_slides: int
    slider_length: float

    spinner_end_time: int

    timing_beat_length: float
    timing_meter: int
    timing_uninherited: bool
