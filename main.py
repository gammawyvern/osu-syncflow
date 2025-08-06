from typing import Dict, List

from utils import file_parser, line_parser, data_parser

from models import TimingPoint, HitObject, OsuDataFrame

def main():
    with open("./assets/reanimate.osu", 'r', encoding="utf-8") as file:
        file_content: str = file.read()

    sections: Dict[str, list] = file_parser.get_sections(file_content)

    # Timing Point Setup

    timing_point_lines: List[str] = sections.get("TimingPoints")
    timing_points: List[TimingPoint] = [line_parser.parse_timing_point_line(line) for line in timing_point_lines]

    # Hit Object Setup

    hit_object_lines: List[str] = sections.get("HitObjects")
    hit_objects: List[HitObject] = [line_parser.parse_hit_object_line(line) for line in hit_object_lines]

    # Data Frame Setup

    data_frames: List[OsuDataFrame] = data_parser.combine_timing_points_with_hit_objects(timing_points, hit_objects)



if __name__ == "__main__":
    main()

