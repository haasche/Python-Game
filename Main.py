#!/usr/bin/env python3
import tcod

from Engine import Engine
from Input_handlers import EventHandler
from Game_Map import GameMap
from Entity import Entity

def main():
   screen_width = 80
   screen_height = 50

   map_width = 80
   map_height = 45

   #loads the font used for the game
   tileset = tcod.tileset.load_tilesheet(
      "textImage.png", 32, 8, tcod.tileset.CHARMAP_TCOD
   )

   #create an event_handler object
   event_handler = EventHandler()

   #create a player, npc object
   player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255,255,255))
   npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255,255,0))
   entities = {npc, player}

   Game_Map = GameMap (map_width, map_height)

   #now running graphics through engine
   engine = Engine(entities=entities, event_handler=event_handler, Game_Map=Game_Map, player=player)


   with tcod.context.new_terminal(
      screen_width,
      screen_height,
      tileset = tileset,
      title="Gamiest Game Ever",
      vsync = True,
   ) as context:
      root_console = tcod.Console(screen_width, screen_height, order="F")
      while True:
         engine.render(console = root_console, context = context)
         events = tcod.event.wait()
         engine.handle_events(events)
         context.present(root_console)

if __name__ == "__main__":
      main()