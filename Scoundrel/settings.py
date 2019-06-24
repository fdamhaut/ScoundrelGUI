# Player
MAX_LIFE = 20
STARTING_WPN = [0, -1]

# Game
CARDS = list(range(52))
BANNED_CARDS = {35, 36, 37, 38, 48, 49, 50, 51}     # Depends on the Game Rule, Here Red Figures
CARDS_SUIT_NAME = {0: 'Spades', 1: 'Clubs', 2: 'Diamonds', 3: 'Hearts'}
CARDS_SUIT = {0: 'S', 1: 'C', 2: 'D', 3: 'H'}
CARDS_EVENT = {0: 'Fight against', 1: 'Fight against', 2: 'Equip', 3: 'Heal yourself with'}