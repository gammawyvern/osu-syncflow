from typing import Dict, List

from models import TimingPoint
from utils import file_parser

def main():
    with open("./assets/reanimate.osu", 'r', encoding="utf-8") as file:
        file_content: str = file.read()

    sections: Dict[str, list] = file_parser.get_sections(file_content)

    # Timing Point Setup

    timing_point_lines: List[str] = sections.get("TimingPoints")
    timing_points: List[TimingPoint] = [TimingPoint.from_line(line) for line in timing_point_lines]

    # Hit Object Setup

    hit_object_lines: List[str] = sections.get("HitObjects")

if __name__ == "__main__":
    main()

