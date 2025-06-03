from typing import List
from enum import Enum
import re

class Header(Enum):
    HEADER_PATTERN: str = r"^\[.*\]$"

    HIT_OBJECTS: str = "[HitObjects]"
    TIMING_POINTS: str = "[TimingPoints]"

def get_section(osu_file: str, header: Header) -> List[str]:
    lines: List[str] = [line for line in osu_file.splitlines() if line.strip()]

    header_index: int = lines.index(header.value)

    next_header_pattern = re.compile(Header.HEADER_PATTERN.value)
    for i in range(header_index + 1, len(lines)):
        if next_header_pattern.match(lines[i]):
            next_header_index = i
            break
    else:
        next_header_index = len(lines)


    return lines[header_index + 1:next_header_index]

