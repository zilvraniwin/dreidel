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
    def __init__(self, name, pot_size=0):
        self.name = name
        self.pot_size = pot_size