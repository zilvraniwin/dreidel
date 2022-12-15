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


class DreidelGame:

    def __init__(self, input_text=None, default_player_pot=10, starting_pot=0):
        """Initialize a dreidel game, starting with a user-given list of
        players and a default pot size per player of 10 gelt.
        """
        self.sides = [
            ("nun", "Nun: Nothing! Next!"),
            ("gimel", "Gimel: Gimme all the gelt!"),
            ("hey", "Hey: Take half!"),
            ("shin", "Shin: Put one in!")
        ]
        self.current_state = None
        if input_text:
            self.input_text = input_text
        else:
            self.input_text = input("Who's playing?\n> ")
        self.default_player_pot = default_player_pot
        self.parse_input()
        self.pot = starting_pot
        self.position = 0

    def parse_input(self):
        """Parse the user-given input into player objects."""
        split_players = self.input_text.split(sep=",")
        self.players = [Player(*self.get_player_pot(player)) for player in
         split_players]

    def get_player_pot(self, player_string):
        """Determine whether a starting pot size was provided, and if
        not, use the default."""
        pot_regex = re.search("(?<=\()[0-9]+", player_string)
        if pot_regex:
            player_name = player_string.split(sep=" (")[0].strip()
            pot_size = int(pot_regex[0])
        else:
            player_name = player_string.strip()
            pot_size = self.default_player_pot
        return player_name, pot_size

    def ante(self):
        """At the start of a round, all players add one to the main pot,
        or, if they cannot, they are removed from the game."""
        print("Ante up!")
        for player in self.players:
            if player.pot > 0:
                player.pot -= 1
                self.pot += 1
                print(f"{player.name}: {player.pot}")
            else:
                print(f"{player.name} cannot ante up. {player.name} is out!")
                self.players.remove(player.name)
        print(f"\nCurrent pot: {self.pot}")

    def turn(self, player):
        """Have a player spin the dreidel; adjust their pot and the
        group pot accordingly.
        """
        print(f"\n{player.name}'s turn.")
        print(f"{player.name} spins the dreidel...")
        self.spin_dreidel()
        side = self.current_state[0]
        print(self.current_state[1])
        if side == "nun":
            None
        elif side == "gimel":
            player.pot += self.pot
            self.pot = 0
        elif side == "hey":
            # Player gets half rounded up on a hey.
            if self.pot % 2 == 0:
                player.pot += self.pot // 2
                self.pot //= 2
            else:
                player.pot += self.pot // 2 + 1
                self.pot //= 2
        elif side == "shin":
            if player.pot > 0:
                player.pot -= 1
                self.pot += 1
            else:
                print(f"{player.name} cannot put one in.")
        else:
            print("Well that's not a side I'm familiar with.")
        print(f"{player.name}: {player.pot}")
        print(f"\nCurrent pot: {self.pot}")

    def round(self):
        print("\nNew round.")
        self.ante()
        # for player in self.players:
        #     self.turn(player)
        while self.pot > 0:
            self.turn(self.players[self.position])
            if self.position < len(self.players) - 1:
                self.position += 1
            else:
                self.position = 0
        print("\nPot is empty. End of round.")

    def spin_dreidel(self):
        """Spin the dreidel!"""
        spin = rd.randint(0, 3)
        self.current_state = self.sides[spin]
