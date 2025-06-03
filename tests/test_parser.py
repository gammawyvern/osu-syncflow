from osu_syncflow.parser import Header, get_section

def test_basic_section_extraction(test_osu_file_path: str):
    print(f"In extraction test: {test_osu_file_path}")
    with open(test_osu_file_path, 'r') as osu_file:
        test_osu_file: str = osu_file.read()

    actual_timing_point_lines = get_section(test_osu_file, Header.TIMING_POINTS)
    actual_hit_object_lines = get_section(test_osu_file, Header.HIT_OBJECTS)

    expected_timing_point_length: int = 84
    expected_hit_object_length: int = 380 

    assert len(actual_timing_point_lines) == expected_timing_point_length
    assert len(actual_hit_object_lines) == expected_hit_object_length

