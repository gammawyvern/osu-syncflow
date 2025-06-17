from typing import List
import pytest

from osu_syncflow.file.read import read_osu_file, read_osu_file_sections


EXPECTED_OSU_SECTIONS: List[str] = [
    "",
    "[General]",
    "[Editor]",
    "[Metadata]",
    "[Difficulty]",
    "[Events]",
    "[TimingPoints]",
    "[Colours]",
    "[HitObjects]"
]


def test_read_osu_file_valid(test_osu_file_path: str):
    osu_file_contents: str = read_osu_file(test_osu_file_path)
    for section in EXPECTED_OSU_SECTIONS:
        assert section in osu_file_contents

def test_read_osu_file_non_osu_file(test_osu_audio_path: str):
    with pytest.raises(ValueError):
        osu_file_contents: str = read_osu_file(test_osu_audio_path)

def test_read_osu_file_dne():
    with pytest.raises(ValueError):
        osu_file_contents: str = read_osu_file("assets/dne/test.osu")

