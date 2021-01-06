from __future__ import annotations

from typing import Tuple, TYPE_CHECKING

import color

if TYPE_CHECKING:
    from tcod import Console
    from engine import Engine
    from game_map import GameMap


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""

    names = ", ".join(
        entity.name for entity in game_map.entities if entity.x == x and entity.y == y
    )

    return names.capitalize()


def render_bar(
    console: Console, current_value: int, maximum_value: int, total_width: int
) -> None:
    bar_width = int(float(current_value) / maximum_value * total_width)

    console.draw_rect(x=0, y=45, width=20, height=1, ch=1, bg=color.bar_empty)

    if bar_width > 0:
        console.draw_rect(
            x=0, y=45, width=bar_width, height=1, ch=1, bg=color.bar_filled
        )

    console.print(
        x=0, y=45, string=f"Fortitude: {current_value}/{maximum_value}", fg=color.bar_text
    )


def render_dungeon_level(
    console: Console, dungeon_level: int, location: Tuple[int, int], engine: Engine
) -> None:
    """
    Render the level the player is currently on, at the given location.
    """
    x, y = location

    if dungeon_level > 9:
        console.print(x=x, y=y, string=f"Death")
    elif dungeon_level == 1:
        console.print(x=x, y=y, string=f"Unease")

    elif dungeon_level == 2:
        console.print(x=x, y=y, string=f"Distress")
    elif dungeon_level == 3:
        console.print(x=x, y=y, string=f"Despair")
    elif dungeon_level == 4:
        console.print(x=x, y=y, string=f"Mania")
    elif dungeon_level == 5:
        console.print(x=x, y=y, string=f"Delusion")
    elif dungeon_level == 6:
        console.print(x=x, y=y, string=f"Hysteria")
    elif dungeon_level == 7:
        console.print(x=x, y=y, string=f"Lunacy")
    elif dungeon_level == 8:
        console.print(x=x, y=y, string=f"Derangement")
    elif dungeon_level == 9:
        console.print(x=x, y=y, string=f"Decay")
    else:
        console.print(x=x, y=y, string=f"Floor {dungeon_level}")


def render_names_at_mouse_location(
    console: Console, x: int, y: int, engine: Engine
) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(
        x=mouse_x, y=mouse_y, game_map=engine.game_map
    )

    console.print(x=x, y=y, string=names_at_mouse_location)
