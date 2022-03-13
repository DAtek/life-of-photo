from functools import lru_cache
from pathlib import Path
import numpy as np
from cv2 import cv2


_BASE_DIR = Path(__file__).resolve().parent


class ImageReader:
    def __set_name__(self, owner, name):
        self._filename = f"{name}.png"

    @lru_cache
    def __call__(self) -> np.ndarray:
        return cv2.imread(str(_BASE_DIR / self._filename), cv2.IMREAD_GRAYSCALE)


class ImageCollection:
    overpopulation_end = ImageReader()
    overpopulation_start = ImageReader()
    populate_end = ImageReader()
    populate_start = ImageReader()
    solitude_end = ImageReader()
    solitude_start = ImageReader()
    survive_end = ImageReader()
    survive_start = ImageReader()
