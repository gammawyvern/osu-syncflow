from dataclasses import dataclass
from typing import List
from enum import Enum
from abc import ABC

''' Simple classes for use. '''

@dataclass
class CurvePoint:
    x: int
    y: int
    
    def __str__(self):
        return f"{self.x}:{self.y}"

@dataclass
class EdgeSet:
    normal_set: int
    additional_set: int

    def __str__(self):
        return f"{self.normal_set}:{self.additional_set}"

@dataclass
class HitSample:
    samples: List[int]

    def __str__(self):
        return ''.join(map(lambda sample: f"{sample}:", self.samples)) 

''' Additional hit object params. '''

class HitObjectParams:
    def __str__(self):
        return ""

class SliderObjectParams(HitObjectParams):
    curve_type: str # char
    curve_points: List[CurvePoint]
    slides: int
    length: float
    edge_sounds: List[int]
    edge_sets: List[EdgeSet]

    def __str__(self):
        ''' TODO: Not sure if this works, since the arrays are not str. FIXME '''
        curve_points_str: str = '|'.join(self.curve_points)
        edge_sounds_str: str = '|'.join(self.edge_sounds)
        edge_sets_str: str = '|'.join(self.edge_sets)
        return f"{self.curve_type}|{curve_points_str},{self.slides},{self.length},{edge_sounds_str},{edge_sets_str}"

class SpinnerObjectParams(HitObjectParams):
    end_time: int

    def __str__(self):
        return f"{self.end_time}"

''' Final HitObject class. '''

@dataclass
class HitObject:
    x: int
    y: int
    time: int
    type: int
    hit_sound: int
    params: HitObjectParams
    hit_sample: HitSample

    def __str__(self):
        return f"{self.x},{self.y},{self.type.value},{self.hit_sound},{self.params},{self.hit_sample}"

