#!/usr/bin/env python

import random as rd
import re


class Player:
    
    def __init__(self, name, pot_size):
        """Initialize a dreidel player. Give them a name and a pot size,
        which defaults to 10 in the DreidelGame class.
        """
        self.name = name
        self.pot_size = pot_size
        print(self.name, self.pot_size)


class DreidelGame:

    def __init__(self, input_text, default_pot_size=10):
        """Initialize a dreidel game, starting with a user-given list of
        players and a default pot size per player of 10 gelt.
        """
        # self.players = players
        self.sides = [
            ("nun", "Nun: Nothing! Next!"),
            ("gimel", "Gimel: Gimme all the gelt!"),
            ("hey", "Hey: Take half!"),
            ("shin", "Shin: Put one in!")
        ]
        self.current_state = None
        self.input_text = input_text
        self.default_pot_size = default_pot_size
        self.parse_input()

    def parse_input(self):
        """Parse the user-given input into player objects."""
        split_players = self.input_text.split(sep=",")
        self.players = [Player(*self.get_pot(player)) for player in split_players]

    def get_pot(self, player_string):
        pot_regex = re.search("(?<=\()[0-9]+", player_string)
        if pot_regex:
            player_name = player_string.split(sep=" (")[0].strip()
            pot_size = int(pot_regex[0])
        else:
            player_name = player_string.strip()
            pot_size = self.default_pot_size
        return player_name, pot_size

    def spin_dreidel(self):
        """Spin the dreidel! Return a double of the result and its
        corresponding text.
        """
        spin = rd.randint(0, 3)
        self.current_state = self.sides[spin]