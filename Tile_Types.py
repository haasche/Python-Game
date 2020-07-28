from typing import Tuple

import numpy as np #type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
   [
      ("ch", np.int32), # Unicode codepoint (ch = character)
      ("fg", "3B"), # 3 unsigned bytes, RGB colors (fg = foreground)
      ("bg", "3B"), # (bg = background)
   ]
)

# Tile struct used for dstatically defined tile data
tile_dt = np.dtype(
   [
      ("walkable", np.bool), # If true, tile can be walked on 
      ("transparent", np.bool), # If true, tile does NOT block FOV 
      ("dark", graphic_dt), # Graphics for when this tile is not in FOV
   ]
)

def new_tile(
   *, # Enforce the use of keywords so that parameter order doesn't matter
   walkable: int,
   transparent: int,
   dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
      """Helper function for defining individual tile types """
      return np.array((walkable, transparent, dark), dtype = tile_dt)

# Floor should be walkable
floor = new_tile(
   walkable = True, transparent = True, dark = (ord(" "), (255, 255, 255), (50, 50, 150)),
)

# Walls are solid, thus you can not phase through them
wall = new_tile(
   walkable = False, transparent = False, dark = (ord(" "), (255, 255, 255), (0, 0, 100)),
)