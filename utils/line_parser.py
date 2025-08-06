from typing import List, Tuple, Dict

from models.timing_point import TimingPoint
from models.hit_object import HitObject


# Timing Point Parsing

def parse_timing_point_line(line: str) -> TimingPoint:
    values: List[str] = line.split(',')
    if len(values) != 8:
        raise Exception(f"Timing point line was incorrect: {values}")

    return TimingPoint(
        time=int(values[0]),
        beat_length=float(values[1]),
        meter=int(values[2]),
        uninherited=bool(int(values[6])),
    )


# Hit Object Parsing

def __parse_hit_circle_from_line(line: str) -> HitObject:
    chunks: List[str] = line.split(',')

    return HitObject(
        x=int(chunks[0]),
        y=int(chunks[1]),
        time=int(chunks[2]),
        type=int(chunks[3]),

        slider_type=int(-1),
        slider_slides=int(-1),
        slider_length=int(-1),

        spinner_end_time=int(-1)
    )


def __parse_slider_from_line(line: str) -> List[HitObject]:
    chunks: List[str] = line.split(',')
    curve_chunks: List[str] = chunks[5].split('|')
    curve_type: int = int(curve_chunks[0])
    curve_points: List[Tuple[int, int]] = [(int(chunks[0]), int(chunks[1]))] + [
        tuple(map(int, xy_str.split(':'))) for xy_str in curve_chunks[1].split(',')
    ]

    return [
        HitObject(
            x=xy_pair[0],
            y=xy_pair[1],
            time=int(chunks[2]),
            type=int(chunks[3]),

            slider_type=curve_type,
            slider_slides=int(chunks[6]),
            slider_length=float(chunks[7]),

            spinner_end_time=int(-1)
        ) for xy_pair in curve_points
    ]


def __parse_spinner_from_line(line: str) -> HitObject:
    chunks: List[str] = line.split(',')

    return HitObject(
        x=int(chunks[0]),
        y=int(chunks[1]),
        time=int(chunks[2]),
        type=int(chunks[3]),

        slider_type=int(-1),
        slider_slides=int(-1),
        slider_length=int(-1),

        spinner_end_time=int(chunks[5])
    )


# Parse Hit Object Line Automatically

NOTE_BIT = 1 << 0
SLIDER_BIT = 1 << 1
SPINNER_BIT = 1 << 3

TYPE_PARSER_MAP: Dict[int, callable] = {
    NOTE_BIT: __parse_hit_circle_from_line,
    SLIDER_BIT: __parse_slider_from_line,
    SPINNER_BIT: __parse_spinner_from_line,
}


def parse_hit_object_line(line: str) -> HitObject | List[HitObject]:
    chunks: List[str] = line.split(',')
    type: int = int(chunks[3])

    for type_flag_bit, parser_func in TYPE_PARSER_MAP.items():
        if type & type_flag_bit:
            return parser_func(line)

    raise ValueError(f"Line type wasn't valid\n\t{type}")
