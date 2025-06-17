from dataclasses import dataclass
from typing import List
import re

from osu_syncflow.beatmap.timing_point import TimingPoint
from osu_syncflow.beatmap.hit_object import HitObject


@dataclass
class Beatmap:
    timing_points: List[TimingPoint]
    hit_objects: List[HitObject]

