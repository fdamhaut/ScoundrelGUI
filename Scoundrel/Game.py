from Scoundrel import Deck as d, settings as s, Player as p


class Scoundrel:

    # Setup
    seed = None

    # Data
    player = p.Player()
    deck = None
    deckstatus = True
    lockroom = False

    # Action events
    event = {
        0: player.fight,
        1: player.fight,
        2: player.equip,
        3: player.heal
    }

    # Game status
    alive = True
    win = False
    n0turn = 0
    score = 0
    room = []

    def __init__(self, autoplay=False, seed=None):
        self.seed = seed
        self.deck = d.Deck(seed)
        self.refill()
        print('A')
        if autoplay:
            self.play()

    def __repr__(self):
        return "A game of Scoundrel"

    # Full play
    def play(self):

        while self.alive and len(self.room) > 1:
            self.alive = self.act(self.getaction())

        self.score += self.player.score() + self.deck.score() + self.roomscore()
        print("Your score is ", self.score)

        return self.score

    # Game mechanics
    def act(self, action):

        # You still need to play
        if not self.alive:
            return False

        self.n0turn += 1

        if action == 5:
            self.leave()
            self.lockroom = True
        else:
            self.lockroom = False
            if not self.encounter(self.room.pop(action-1)):
                return False

        if len(self.room) < 2:
            self.refill()

        return True

    def refill(self):
        while len(self.room) < 4 and self.deckstatus:
            self.deckstatus, card = self.deck.draw()
            if card in s.BANNED_CARDS:
                continue
            self.room.append(card)

    def canleave(self):
        return not self.lockroom and len(self.room) == 4

    def leave(self):
        for r in self.room:
            self.deck.back(r)
        self.room = []

    def encounter(self, card):
        return self.event[d.suit(card)](d.value(card))

    def roomscore(self):
        score = 0
        for c in self.room:
            if d.suit(c) in {0, 1}:
                score -= d.value(c)
        return score

    # Human interactions
    def getaction(self):
        self.printInfo()
        action = int(input())
        while not((0 < action < len(self.room)+1) or (action == 5 and self.canleave())):
            print(action, "is an incorrect action, try again !")
            action = int(input())
        return action

    def printInfo(self):
        print("Turn #", self.n0turn)
        print(self.player)
        print("In your room you can see", self.deck)
        print("Would you like to;")
        for i, c in enumerate(self.room, 1):
            print(i, ")", s.CARDS_EVENT[d.suit(c)], d.card2str(c))
        if self.canleave():
            print("Or leave(5) ?")
