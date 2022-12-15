# Dreidel

> A little mostly-automated dreidel game for python.

## How to play

Load in the module in your preferred interactive manner (e.g., iPython: `%run dreidel.py`).

Initialize an instance of the `DreidelGame` class, optionally providing:
- A string of players, comma-separated, with their respective pot sizes in parentheses, or use the default pot size
- A starting player pot size to use if not provided in the player string to (defaults to 10)
- The starting group pot size (defaults to 0)

If you don't provide players when initializing the class, it will ask.

```ipython
In [1]: d = DreidelGame()
Who's playing?
> Zilvra (10), Enna, Margo (15), Barion (20)
```

Then run a round using `DreidelGame.round()` which will handle the ante (each player adds 1 to the group pot) and each player's turn on the dreidel. If a player has 0 in their pot at the start of the round and cannot put in their ante, they are removed from the game.

```ipython
In [2]: d.round()

New round.
Ante up!
Zilvra: 9
Enna: 9
Margo: 14
Barion: 19

Current pot: 4

Zilvra's turn.
Zilvra spins the dreidel...
Gimel: Gimme all the gelt!
Zilvra: 13

Current pot: 0

Enna's turn.
Enna spins the dreidel...
Nun: Nothing! Next!
Enna: 9

Current pot: 0

Margo's turn.
Margo spins the dreidel...
Nun: Nothing! Next!
Margo: 14

Current pot: 0

Barion's turn.
Barion spins the dreidel...
Shin: Put one in!
Barion: 18

Current pot: 1

End of round.
```

Continue until there's only one player left who gets the whole pot, or quit and mark down the pot sizes to come back to later.