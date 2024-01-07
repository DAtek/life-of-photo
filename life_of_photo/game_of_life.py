from typing import Iterator

import numpy as np

LIVING_MAP = np.zeros(256, np.uint8)
LIVING_MAP[255] = 1

SPAWN_DIE_NEIGHBOURS_MAP = np.zeros(9, np.uint8)

# DIE
SPAWN_DIE_NEIGHBOURS_MAP[:2] = 2
SPAWN_DIE_NEIGHBOURS_MAP[4:] = 2

# SPAWN
SPAWN_DIE_NEIGHBOURS_MAP[3] = 4

MASK_LIVE_MAP = np.zeros(8, np.uint8)
MASK_LIVE_MAP[4:6] = 255
MASK_LIVE_MAP[1] = 255


MASK_BOOL_MAP = np.ones(256, np.uint8)
MASK_BOOL_MAP[0] = 0


class GameOfLife(Iterator):
    def __init__(self, world: np.ndarray):
        self._new_world: np.ndarray = np.copy(world)
        self._world = world
        self._coordinates = [
            (i, j)
            for i in range(self._world.shape[0])
            for j in range(self._world.shape[1])
        ]

    def __next__(self) -> np.ndarray:
        self._simulate_next()
        self._world = np.copy(self._new_world)
        return self._new_world

    def _simulate_next(self):
        neighbours_map = np.zeros(self._world.shape, np.uint8)
        living_cells_world = LIVING_MAP[self._world]

        for i, j in self._coordinates:
            neighbours_map[i, j] = np.sum(
                living_cells_world[
                    i - 1 : i + 2,
                    j - 1 : j + 2,
                ]
            )

        neighbours_map -= MASK_BOOL_MAP[neighbours_map] & living_cells_world
        spawn_die = SPAWN_DIE_NEIGHBOURS_MAP[neighbours_map]
        masked_map = spawn_die + living_cells_world
        self._new_world = MASK_LIVE_MAP[masked_map]
