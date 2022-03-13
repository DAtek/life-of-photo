from dataclasses import dataclass
import numpy as np
from cv2 import cv2
from pytest import mark, param

from life_of_photo.game_of_life import GameOfLife
from tests.examples import ImageCollection, ImageReader


class TestGameOfLife:
    @mark.parametrize(
        ["start", "end"],
        [
            param(
                ImageCollection.survive_start, ImageCollection.survive_end, id="survive"
            ),
            param(
                ImageCollection.solitude_start,
                ImageCollection.solitude_end,
                id="solitude",
            ),
            param(
                ImageCollection.overpopulation_start,
                ImageCollection.overpopulation_end,
                id="overpopulation",
            ),
            param(
                ImageCollection.populate_start,
                ImageCollection.populate_end,
                id="populate",
            ),
        ],
    )
    def test_iteration(self, start: ImageReader, end: ImageReader):
        game = GameOfLife(start())
        expected_image = end()

        end_image = next(game)
        diff = np.sum((cv2.absdiff(end_image, expected_image)))
        # cv2.imshow("result", end_image)
        # cv2.imshow("expected", expected_image)
        # cv2.imshow("start", start())
        # cv2.waitKey()
        assert diff == 0


@dataclass
class Scenario:
    name: str
    start_state: np.ndarray
    end_state: np.ndarray
