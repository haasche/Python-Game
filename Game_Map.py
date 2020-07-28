import numpy as np # type: ignore
from tcod.console import Console

import Tile_Types

class GameMap:
   # initalizer takes width/height and assigns them
   def __init__(self, width: int, height: int):
      self.width, self.height = width, height
      self.tiles = np.full((width, height), fill_value = Tile_Types.floor, order = "F")
      self.tiles[30:33, 22] = Tile_Types.wall # hard coded wall for testing purposes

   # Returns True if player is in bound
   def in_bounds (self, x:int, y:int) -> bool:
      """Return True if x and y are inside of the bounds of this map."""
      return 0 <= x < self.width and 0 <= y < self.height

   # Faster way to render the map rather than printing 
   def render(self, console: Console) -> None:
      console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
