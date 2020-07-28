from typing import Tuple

class Entity:
   """
   A generic object to represent players, enemies, items, etc.
   """
   #initializer that has the x,y coordinates, the character, and the color of the entity (R,G,B)
   def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
      self.x = x
      self.y = y
      self.char = char
      self.color = color
      
   #takes dx and dy and modifies the entity's position
   def move(self, dx: int, dy: int) -> None:
      self.x += dx
      self.y += dy
