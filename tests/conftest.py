from pathlib import Path

from pytest import fixture
import pytest

@fixture(scope="session")
def assets_dir() -> Path:
    return Path(__file__).parent.parent / "assets"

@fixture
def test_osu_file_path(assets_dir) -> Path:
    return assets_dir / "reanimate" / "reanimate.osu"

@fixture
def test_osu_audio_path(assets_dir) -> Path:
    return assets_dir / "reanimate" / "reanimate.mp3"

