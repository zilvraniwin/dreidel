#!/usr/bin/env python3

import random as rd


def spin_dreidel():
    results = [
        ("nun", "Nun: Nothing! Next!"),
        ("gimel", "Gimel: Gimme all the gelt!"),
        ("hey", "Hey: Take half!"),
        ("shin", "Shin: Put one in!")
    ]
    spin = rd.randint(0, 3)
    return results[spin]


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

    