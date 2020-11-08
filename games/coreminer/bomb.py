# Bomb: A Bomb in the game.

# DO NOT MODIFY THIS FILE
# Never try to directly create an instance of this class, or modify its member variables.
# Instead, you should only be reading its variables and calling its functions.

from typing import Optional
from games.coreminer.game_object import GameObject

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add additional import(s) here
# <<-- /Creer-Merge: imports -->>

class Bomb(GameObject):
    """The class representing the Bomb in the Coreminer game.

    A Bomb in the game.
    """

    def __init__(self):
        """Initializes a Bomb with basic logic as provided by the Creer code generator.
        """
        GameObject.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._tile = None
        self._timer = 5

    @property
    def tile(self) -> Optional['games.coreminer.tile.Tile']:
        """games.coreminer.tile.Tile or None: The Tile this Bomb is on.
        """
        return self._tile

    @property
    def timer(self) -> int:
        """int: The number of turns before this Bomb explodes. One means it will explode after the current turn.
        """
        return self._timer


    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>
