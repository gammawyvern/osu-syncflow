from typing import List

from models import TimingPoint, HitObject, OsuDataFrame


def combine_timing_points_with_hit_objects(timing_points: List[TimingPoint], hit_objects: List[HitObject]) -> List[OsuDataFrame]:
    timing_point_index = 0
    result: List[OsuDataFrame] = []

    for hit_object in hit_objects:
        while timing_point_index + 1 < len(timing_points) and timing_points[timing_point_index + 1].time <= hit_object.time:
            timing_point_index += 1

        timing_point = timing_points[timing_point_index]

        result.append(
            OsuDataFrame(
                x=hit_object.x,
                y=hit_object.y,
                time=hit_object.time,
                type=hit_object.type,

                slider_type=hit_object.slider_type,
                slider_slides=hit_object.slider_slides,
                slider_length=hit_object.slider_length,

                spinner_end_time=hit_object.spinner_end_time,

                timing_beat_length= timing_point.beat_length,
                timing_meter=timing_point.meter,
                timing_uninherited=timing_point.uninherited,
            )
        )

    return result
