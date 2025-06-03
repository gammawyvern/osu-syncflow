
def test_osu_loading(test_osu_file_path: str):
    print(f"Resolved path: {test_osu_file_path}")
    assert test_osu_file_path.exists()

