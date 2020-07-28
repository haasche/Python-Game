from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from Entity import Entity
from Game_Map import GameMap
from Input_handlers import EventHandler


class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, Game_Map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = Game_Map
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()