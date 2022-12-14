#!/usr/bin/env python

import random as rd


class Player:
    
    def __init__(self, name, pot_size=10):
        """Initialize a dreidel player. Give them a name and a pot size,
        which defaults to 10.
        """
        self.name = name
        self.pot_size = pot_size


class DreidelGame:

    def __init__(self, players):
        """Initialize a dreidel game, passing a list of player objects."""
        self.players = players
        self.sides = [
            ("nun", "Nun: Nothing! Next!"),
            ("gimel", "Gimel: Gimme all the gelt!"),
            ("hey", "Hey: Take half!"),
            ("shin", "Shin: Put one in!")
        ]
        self.current_state = None

    def spin_dreidel(self):
        """Spin the dreidel! Return a double of the result and its
        corresponding text.
        """
        spin = rd.randint(0, 3)
        self.current_state = self.sides[spin]
