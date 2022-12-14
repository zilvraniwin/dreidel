#!/usr/bin/env python

import random as rd
import re


class Player:
    
    def __init__(self, name, pot):
        """Initialize a dreidel player. Give them a name and a pot size,
        which defaults to 10 in the DreidelGame class.
        """
        self.name = name
        self.pot = pot
        # print(self.name, self.pot_size)


class DreidelGame:

    def __init__(self, input_text, default_player_pot=10, starting_pot=0):
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
        self.default_player_pot = default_player_pot
        self.parse_input()
        self.pot = starting_pot

    def parse_input(self):
        """Parse the user-given input into player objects."""
        split_players = self.input_text.split(sep=",")
        self.players = [Player(*self.get_player_pot(player)) for player in
         split_players]

    def get_player_pot(self, player_string):
        pot_regex = re.search("(?<=\()[0-9]+", player_string)
        if pot_regex:
            player_name = player_string.split(sep=" (")[0].strip()
            pot_size = int(pot_regex[0])
        else:
            player_name = player_string.strip()
            pot_size = self.default_player_pot
        return player_name, pot_size

    def ante(self):
        for player in self.players:
            if player.pot > 0:
                player.pot -= 1
                self.pot += 1
                print(f"{player.name}: {player.pot}")
            else:
                print(f"{player.name} cannot ante up!")
        print(f"\nCurrent pot: {self.pot}")

    def spin_dreidel(self):
        """Spin the dreidel! Return a double of the result and its
        corresponding text.
        """
        spin = rd.randint(0, 3)
        self.current_state = self.sides[spin]