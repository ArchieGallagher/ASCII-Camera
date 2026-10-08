import pytest
import numpy as np
from unittest.mock import MagicMock

from project import img_downscaler
from project import get_current_frame_array
from project import get_brightness_ascii

def test_img_downscaler():
    test_frame = np.zeros((720, 1280, 3), dtype=np.unit8)
    result = img_downscaler(test_frame)
    assert result.shape == (60, 120, 3)
    assert reesult.dtype == np.uint8

    flat_frame = np.full((720, 1280, 3), (10, 120, 250), dtype=np.uint8)
    flat_result = img_downscaler(flat_frame)
    assert np.all(flat_result == (10, 120, 250))

def test_get_current_frame_array():
    test_frame = np.zeros((720, 1280, 3), dtype=np.uint8)
    video = MagicMock()
    video.read.return_value = (True, test_frame)
    assert get_current_frame_array(0, video) is test_frame

    video.read.return_value = (False, None)
    with pytest.raises(ValueError):
        get_current_frame_array(0, video)

def test_get_brightness_ascii():
    #Example3
    assert get_brightness_ascii(0, 0, 0) == "."
    assert get_brightness_ascii(255, 255, 255) == "@"
    assert get_brightness_ascii(128, 128, 128) == "+"

    #For the weighted channels
    blue = get_brightness_ascii(255, 0, 0)
    green = get_brightness_ascii(0, 255, 0)
    red = get_brightness_ascii(0, 0, 255)
    ramp = ".:-=+*#%@"
    assert ramp.index(green) > ramp.index(red) > ramp.index(blue)

    #Returns only one character
    for value in (0, 50, 100, 200, 255):
        result = get_brightness_ascii(value, value, value)
        assert len(result) ==1
        assert result in ramp
