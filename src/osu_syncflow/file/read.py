from dataclasses import dataclass
from pathlib import Path
from typing import List
import re


@dataclass
class OsuFileSection:
    title: str
    lines: List[str]


def read_osu_file(osu_file_path: str) -> str:
    osu_file_path = Path(osu_file_path)

    if not osu_file_path.exists():
        raise ValueError(f"osu file path does not exist or cannot be accessed: {osu_file_path}")

    if not osu_file_path.name.endswith(""):
        raise ValueError(f"osu file path does not point to .osu file: {osu_file_path}")

    with open(osu_file_path, 'r') as osu_file:
        osu_file_contents: str = osu_file.read()

    return osu_file_contents


def read_osu_file_sections(osu_file: str) -> List[OsuFileSection]:
    lines: List[str] = [line.strip() for line in osu_file.splitlines() if line.strip()]

    section_title_pattern: str = r'^\[\w+\]$'
    sections: List[OsuFileSection] = [
        OsuFileSection(title="", lines=[])
    ]

    for line in lines:
        if re.match(section_title_pattern, line):
            sections.append(OsuFileSection(title=line[1:-1], lines=[]))
        else:
            sections[-1].lines.append(line)

    return sections

